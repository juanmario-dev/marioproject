

from django.db import models
from django.core.exceptions import ValidationError

# -------------------- TERCEROS --------------------
class Tercero(models.Model):
    TIPO_IDENTIFICACION_CHOICES = [
        ('CC', 'C.C'),
        ('NIT', 'NIT'),
        ('CE', 'ID de extranjería'),
    ]

    TIPO_TERCERO_CHOICES = [
        ('Empleado', 'Empleado'),
        ('Proveedor', 'Proveedor'),
        ('Cliente', 'Cliente'),
    ]

    tipo_identificacion = models.CharField(max_length=5, choices=TIPO_IDENTIFICACION_CHOICES)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    tipo_tercero = models.CharField(max_length=20, choices=TIPO_TERCERO_CHOICES)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} - {self.tipo_tercero}"


# -------------------- PLAN DE CUENTAS --------------------
class CuentaContable(models.Model):
    codigo = models.CharField(max_length=20, unique=True, db_index=True)
    nombre = models.CharField(max_length=200)

    movimiento = models.BooleanField(default=False)
    centro_costo = models.BooleanField(default=False)
    criterio1 = models.CharField(max_length=100, blank=True, null=True)
    criterio2 = models.CharField(max_length=100, blank=True, null=True)
    criterio3 = models.CharField(max_length=100, blank=True, null=True)

    nivel = models.PositiveIntegerField(editable=False, default=1)
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='hijos')

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Cuenta contable'
        verbose_name_plural = 'Cuentas contables'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    def clean(self):
        # Jerarquía por cada 2 dígitos en el código
        if not self.codigo or not self.codigo.isdigit():
            raise ValidationError("El código debe ser numérico.")
        if len(self.codigo) % 2 != 0:
            raise ValidationError("La longitud del código debe ser par (2, 4, 6, ...).")

        self.nivel = len(self.codigo) // 2

        if self.nivel > 1:
            parent_code = self.codigo[:-2]
            try:
                padre = CuentaContable.objects.get(codigo=parent_code)
            except CuentaContable.DoesNotExist:
                raise ValidationError(f"Debe existir la cuenta padre con código {parent_code} antes de crear {self.codigo}.")
            self.padre = padre
        else:
            self.padre = None

        if self.padre and self.padre.codigo != self.codigo[:-2]:
            raise ValidationError("El padre no coincide con el prefijo del código.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


# -------------------- DOCUMENTOS CONTABLES --------------------
class DocumentoContable(models.Model):
    codigo = models.CharField(max_length=20, unique=True, db_index=True)
    nombre = models.CharField(max_length=120)
    next_number = models.PositiveIntegerField(default=1)
    padding = models.PositiveSmallIntegerField(default=6)  # ← agrega esta línea

    class Meta:
        ordering = ['codigo']

    def take_next_consecutive(self):
        from django.core.exceptions import ValidationError
        if self.next_number > 999999:
            raise ValidationError("Se agotó el consecutivo (hasta 999999). Cree otro tipo de documento.")
        s = f"{self.next_number:06d}"
        self.next_number += 1
        self.save(update_fields=['next_number'])
        return s


# -------------------- ASIENTO (ENCABEZADO) --------------------
class AsientoContable(models.Model):
    fecha = models.DateField()
    documento = models.ForeignKey(DocumentoContable, on_delete=models.PROTECT, related_name='asientos')
    numero = models.CharField(max_length=12, blank=True, null=True, db_index=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['-fecha', '-id']
        constraints = [
            models.UniqueConstraint(fields=['documento', 'numero'], name='uniq_doc_numero')
        ]

    def ensure_consecutive(self):
        if not self.numero:
            self.numero = self.documento.take_next_consecutive()


# -------------------- MOVIMIENTOS (DETALLE) --------------------
class MovimientoContable(models.Model):
    asiento = models.ForeignKey('AsientoContable', on_delete=models.CASCADE, related_name='movimientos')
    cuenta = models.ForeignKey('CuentaContable', on_delete=models.PROTECT)
    tercero = models.ForeignKey('Tercero', on_delete=models.PROTECT, null=True, blank=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')  # 👈 importante
    debito = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    credito = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    centro_costo = models.BooleanField(default=False)
    criterio1 = models.CharField(max_length=50, blank=True, null=True)
    criterio2 = models.CharField(max_length=50, blank=True, null=True)
    criterio3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']  # o lo que prefieras
        verbose_name = 'Movimiento contable'
        verbose_name_plural = 'Movimientos contables'

    def __str__(self):
        return f"{self.cuenta.codigo} D:{self.debito} C:{self.credito}"



# modelo de inventarios_form.html

# models.py

from django.db import models

class ProductoServicio(models.Model):
    # Identificación
    nombre = models.CharField(max_length=255)
    referencia = models.CharField(max_length=120, blank=True, null=True)

    # Valores comerciales
    precio = models.PositiveIntegerField(default=0)
    descuento_pct = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    impuesto_pct = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    # Activaciones
    causa_fv = models.BooleanField(default=False)
    causa_inventario = models.BooleanField(default=False)

    # Cuentas contables (Factura de venta)
    cta_ingreso = models.ForeignKey(
        'CuentaContable', null=True, blank=True,
        on_delete=models.PROTECT, related_name='ps_cta_ingreso'
    )
    cta_impuestos = models.ForeignKey(
        'CuentaContable', null=True, blank=True,
        on_delete=models.PROTECT, related_name='ps_cta_impuestos'
    )
    cta_cartera = models.ForeignKey(
        'CuentaContable', null=True, blank=True,
        on_delete=models.PROTECT, related_name='ps_cta_cartera'
    )

    # Documento contable
    documento_fv = models.ForeignKey(
        'DocumentoContable', null=True, blank=True,
        on_delete=models.PROTECT, related_name='ps_documento_fv'
    )

    # Inventario / costo
    cta_inventario = models.ForeignKey(
        'CuentaContable', null=True, blank=True,
        on_delete=models.PROTECT, related_name='ps_cta_inventario'
    )
    cta_costo = models.ForeignKey(
        'CuentaContable', null=True, blank=True,
        on_delete=models.PROTECT, related_name='ps_cta_costo'
    )

    doc_fv = models.CharField(max_length=20, blank=True, null=True)
    doc_nc = models.CharField(max_length=20, blank=True, null=True)

    # Estado
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto / Servicio'
        verbose_name_plural = 'Productos / Servicios'

    def __str__(self):
        return self.nombre



# modelo base de datos factura de venta fv_crear.html

from django.db import models
from django.utils import timezone


class FacturaVenta(models.Model):
    # Cabecera
    consecutivo = models.CharField(max_length=20, unique=True)  # "000001"
    fecha_factura = models.DateField(default=timezone.now)
    dias_pago = models.PositiveIntegerField(default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)

    # Cliente (copiado tal cual desde la factura)
    nit = models.CharField(max_length=20)  # sin dígito
    razon_social = models.CharField(max_length=200, blank=True, default="")
    correo = models.EmailField(blank=True, default="")
    direccion = models.CharField(max_length=200, blank=True, default="")

    # Totales (guardados tal cual)
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    iva = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    retenciones = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    abonos = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_pagar = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]

    def __str__(self):
        return f"FV {self.consecutivo} - {self.nit}"


class FacturaVentaLinea(models.Model):
    factura = models.ForeignKey(
        FacturaVenta,
        on_delete=models.CASCADE,
        related_name="lineas"
    )

    descripcion = models.CharField(max_length=500)
    cantidad = models.DecimalField(max_digits=18, decimal_places=2, default=1)

    # Valores de la línea
    precio = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    descuento_pct = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    impuesto_pct = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    total = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.factura.consecutivo} - {self.descripcion}"



# modelo datos_facturacion.html

from django.db import models

class DatosFacturacion(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)
    nit = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    sucursal = models.CharField(max_length=100)
    correo = models.EmailField()

    resolucion_dian = models.CharField(max_length=200)
    resolucion_autoretenedor_dian = models.CharField(max_length=200)
    resolucion_autoretenedor_ica = models.CharField(max_length=200)

    entidades_pago = models.TextField()

    def __str__(self):
        return self.nombre_empresa


# Modelo de nc_crear.html

from decimal import Decimal
from django.db import models

class NotaCredito(models.Model):
    consecutivo = models.CharField(max_length=20, unique=True)
    fecha_nc = models.DateField()
    factura_origen = models.ForeignKey(
        "FacturaVenta",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="notas_credito"
    )

    # tercero (lo mismo que FV)
    nit = models.CharField(max_length=50, blank=True, default="")
    razon_social = models.CharField(max_length=200, blank=True, default="")
    correo = models.CharField(max_length=200, blank=True, default="")
    direccion = models.CharField(max_length=200, blank=True, default="")

    motivo = models.TextField(blank=True, default="")

    subtotal = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"))
    iva = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"))
    total = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal("0"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"NC {self.consecutivo}"


class NotaCreditoLinea(models.Model):
    nota_credito = models.ForeignKey(
        NotaCredito,
        on_delete=models.CASCADE,
        related_name="lineas"
    )

    descripcion = models.CharField(max_length=500)
    cantidad = models.DecimalField(max_digits=18, decimal_places=2, default=1)

    precio = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    descuento_pct = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    impuesto_pct = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    total = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"NC {self.nota_credito.consecutivo} - {self.descripcion}"




# modelo tabla de datos de param_medios_pago.html

# models.py
from django.db import models

class MedioPago(models.Model):
    descripcion = models.CharField(max_length=120)
    entidad_bancaria = models.CharField(max_length=120, blank=True, null=True)
    numero_cuenta = models.CharField(max_length=60, blank=True, null=True)
    cuenta_contable = models.CharField(max_length=30, blank=True, null=True)  # guardamos el "codigo"

    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "medio_pago"
        ordering = ["id"]

    def __str__(self):
        return f"{self.descripcion}"


# modelo tabla de datos de recibo_caja.html

from django.db import models
from django.utils import timezone


class ReciboCaja(models.Model):
    """
    Encabezado del Recibo de Caja
    """
    fecha_elab = models.DateField(default=timezone.now)
    consecutivo = models.CharField(max_length=20, unique=True)  # Ej: RC-000001
    descripcion = models.TextField(blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    contabilizado = models.BooleanField(default=False)
    asiento = models.ForeignKey('AsientoContable', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.consecutivo


class ReciboCajaLinea(models.Model):
    """
    Cada fila del recibo de caja (tabla del frontend)
    """
    recibo = models.ForeignKey(
        ReciboCaja,
        on_delete=models.CASCADE,
        related_name="lineas"
    )

    fecha_pago = models.DateField(blank=True, null=True)
    nit = models.CharField(max_length=30, blank=True, null=True)

    # Por ahora texto; luego lo conectamos a la "lupita" (cartera)
    factura_no = models.CharField(max_length=30, blank=True, null=True)

    # Valores (snapshot)
    valor_factura = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    pago = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    # Medio de pago (id del MedioPago) y su cuenta contable (codigo)
    medio_pago_id = models.IntegerField(blank=True, null=True)
    cuenta_contable = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.recibo.consecutivo} - {self.factura_no or ''}"






# Nomina

# modelo de conceptos_nomina.html

class ConceptoNomina(models.Model):
    TIPO_CHOICES = [
        ('devengos', 'Devengos'),
        ('deducciones', 'Deducciones'),
        ('carga', 'Carga prestacional'),
        ('pago', 'De pago'),
    ]

    codigo = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código"
    )

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre del concepto"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        verbose_name="Tipo de concepto"
    )

    activo = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "nomina_conceptos"  # Nombre claro en SQLite
        verbose_name = "Concepto de Nómina"
        verbose_name_plural = "Conceptos de Nómina"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"



# modelo de parametros_nomina.html

from django.db import models

class ParametroNomina(models.Model):
    CATEGORIA_CHOICES = [
        ("generales", "Datos generales"),
        ("tipos_nomina", "Tipos de Nómina"),
        ("tipos_contrato", "Tipos de contrato"),
        ("areas", "Áreas institucionales"),
        #nuevas
        ("salario_minimo", "Salario mínimo"),
        ("auxilio_transporte", "Auxilio de transporte"),
        ("uvt", "UVT"),
    ]

    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES)
    consecutivo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "nomina_parametros"
        ordering = ["categoria", "consecutivo"]
        constraints = [
            models.UniqueConstraint(fields=["categoria", "consecutivo"], name="uq_parametro_categoria_consecutivo")
        ]

    def __str__(self):
        return f"{self.categoria} | {self.consecutivo} - {self.descripcion}"
    




    
# modelo de parametrizacion_asociacion_conceptos.html


from django.db import models


class NominaParamConcepto(models.Model):
    """
    1 fila por (Tipo de nómina + Concepto).
    Guarda: cuenta, DC, salarial, contracuenta, contratos1..10, etc.
    """
    tipo_nomina = models.ForeignKey(
        "ParametroNomina",
        on_delete=models.CASCADE,
        related_name="param_conceptos_tipo_nomina",
        limit_choices_to={"categoria": "tipos_nomina"},
    )

    concepto = models.ForeignKey(
        "ConceptoNomina",
        on_delete=models.CASCADE,
        related_name="parametrizaciones",
    )

    # Cuenta principal + DC (aplica a todos los tipos)
    cuenta = models.ForeignKey(
        "CuentaContable",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="nomina_param_cuenta",
    )
    dc = models.CharField(
        max_length=1,
        choices=(("D", "Débito"), ("C", "Crédito")),
        null=True,
        blank=True,
    )

    # Solo Devengos
    salarial = models.CharField(
        max_length=2,
        choices=(("SI", "Sí"), ("NO", "No")),
        null=True,
        blank=True,
    )

    # Solo Carga Prestacional (contrapartida + DC2)
    contracuenta = models.ForeignKey(
        "CuentaContable",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="nomina_param_contracuenta",
    )
    dc2 = models.CharField(
        max_length=1,
        choices=(("D", "Débito"), ("C", "Crédito")),
        null=True,
        blank=True,
    )

    # Contratos 1..10 (desde ParametroNomina categoria=tipos_contrato)
    contrato1 = models.ForeignKey(
        "ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL,
        related_name="+", limit_choices_to={"categoria": "tipos_contrato"},
    )
    contrato2 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato3 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato4 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato5 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato6 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato7 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato8 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato9 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})
    contrato10 = models.ForeignKey("ParametroNomina", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", limit_choices_to={"categoria": "tipos_contrato"})

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["tipo_nomina", "concepto"],
                name="uniq_tipo_nomina_concepto",
            )
        ]
        indexes = [
            models.Index(fields=["tipo_nomina"]),
            models.Index(fields=["concepto"]),
        ]

    def __str__(self):
        return f"{self.tipo_nomina} | {self.concepto}"


class NominaParamBase(models.Model):
    """
    Bases de cálculo (modal 🔍): filas (param + devengo).
    Aplica a deducciones y carga (tu JS usa scope ded|car).
    """
    param = models.ForeignKey(
        NominaParamConcepto,
        on_delete=models.CASCADE,
        related_name="bases",
    )
    devengo = models.ForeignKey(
        "ConceptoNomina",
        on_delete=models.CASCADE,
        related_name="+",
        limit_choices_to={"tipo": "devengos"},
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["param", "devengo"],
                name="uniq_param_devengo_base",
            )
        ]

    def __str__(self):
        return f"{self.param_id} base {self.devengo_id}"


class NominaParamTarifa(models.Model):
    """
    Rangos de tarifa (modal %): filas (param + minimo/maximo/pct).
    """
    param = models.ForeignKey(
        NominaParamConcepto,
        on_delete=models.CASCADE,
        related_name="tarifas",
    )
    minimo = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    maximo = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    porcentaje = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)

    orden = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [models.Index(fields=["param"])]
        ordering = ["orden", "id"]

    def __str__(self):
        return f"{self.param_id} [{self.minimo}-{self.maximo}] {self.porcentaje}%"





# modelo de ingreso_personal.html

from django.db import models


class Empleado(models.Model):
    # ===================== DATOS GENERALES =====================
    fecha_ingreso = models.DateField(null=True, blank=True)

    nombre_1 = models.CharField(max_length=80, blank=True)
    nombre_2 = models.CharField(max_length=80, blank=True)
    apellido_1 = models.CharField(max_length=80, blank=True)
    apellido_2 = models.CharField(max_length=80, blank=True)

    cedula = models.CharField(max_length=30, unique=True)
    no_contrato = models.CharField(max_length=40, blank=True)

    tipo_contrato = models.ForeignKey(
        "ParametroNomina",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="empleados_tipo_contrato",
        limit_choices_to={"categoria": "tipos_contrato", "activo": True},
    )

    fecha_terminacion_contrato = models.DateField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    correo_personal = models.EmailField(max_length=120, blank=True)
    correo_institucional = models.EmailField(max_length=120, blank=True)

    telefono_1 = models.CharField(max_length=30, blank=True)
    telefono_2 = models.CharField(max_length=30, blank=True)

    direccion = models.CharField(max_length=180, blank=True)

    # ===================== INFORMACIÓN INSTITUCIONAL =====================
    sueldo = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)

    cargo = models.CharField(max_length=80, blank=True)
    sede = models.CharField(max_length=80, blank=True)
    oficina = models.CharField(max_length=80, blank=True)
    jefe_inmediato = models.CharField(max_length=120, blank=True)

    area = models.ForeignKey(
        "ParametroNomina",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="empleados_area",
        limit_choices_to={"categoria": "areas", "activo": True},
    )

    tipo_nomina = models.ForeignKey(
        "ParametroNomina",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="empleados_tipo_nomina",
        limit_choices_to={"categoria": "tipos_nomina", "activo": True},
    )

    # ===================== CUENTA BANCARIA =====================
    banco_entidad = models.CharField(max_length=120, blank=True)

    BANCO_TIPO_CUENTA_CHOICES = [
        ("corriente", "Corriente"),
        ("ahorro", "Ahorro"),
        ("otro", "Otro"),
    ]
    banco_tipo_cuenta = models.CharField(max_length=20, choices=BANCO_TIPO_CUENTA_CHOICES, blank=True)
    banco_numero_cuenta = models.CharField(max_length=40, blank=True)

    # ===================== ANTECEDENTES / NÚCLEO FAMILIAR =====================
    emergencia_nombre = models.CharField(max_length=120, blank=True)
    emergencia_telefono = models.CharField(max_length=30, blank=True)

    familia_padre = models.CharField(max_length=120, blank=True)
    familia_madre = models.CharField(max_length=120, blank=True)

    # ===================== SEGURIDAD SOCIAL =====================
    salud_entidad = models.CharField(max_length=120, blank=True)
    salud_codigo = models.CharField(max_length=40, blank=True)
    salud_nit = models.CharField(max_length=40, blank=True)

    pension_entidad = models.CharField(max_length=120, blank=True)
    pension_codigo = models.CharField(max_length=40, blank=True)
    pension_nit = models.CharField(max_length=40, blank=True)

    cesantias_entidad = models.CharField(max_length=120, blank=True)
    cesantias_codigo = models.CharField(max_length=40, blank=True)
    cesantias_nit = models.CharField(max_length=40, blank=True)

    ARL_RIESGO_CHOICES = [
        ("0.522", "0.522%"),
        ("1.44", "1.44%"),
        ("2.6", "2.6%"),
        ("4.55", "4.55%"),
    ]
    arl_riesgo = models.CharField(max_length=10, choices=ARL_RIESGO_CHOICES, blank=True)

    # Auditoría
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cedula} - {self.nombre_1} {self.apellido_1}".strip()


def empleado_upload_path(instance, filename):
    ced = instance.empleado.cedula if instance.empleado_id else "sin_cedula"
    return f"empleados/{ced}/{instance.tipo}/{filename}"


class EmpleadoArchivo(models.Model):
    TIPO_CHOICES = [
        ("certificado_bancario", "Certificado bancario"),
        ("antecedentes_policia", "Antecedentes Policía"),
        ("antecedentes_procuraduria", "Antecedentes Procuraduría"),
        ("antecedentes_contraloria", "Antecedentes Contraloría"),
    ]

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="archivos")
    tipo = models.CharField(max_length=40, choices=TIPO_CHOICES)
    archivo = models.FileField(upload_to=empleado_upload_path)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.empleado.cedula} - {self.get_tipo_display()}"


class EmpleadoEducacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="educacion")
    institucion = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.empleado.cedula} - {self.institucion}"


class EmpleadoExperiencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="experiencia")
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.empleado.cedula} - Experiencia"


class EmpleadoHijo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="hijos")
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.empleado.cedula} - {self.nombre}"



from django.db import models

class NovedadNomina(models.Model):
    cedula = models.CharField(max_length=30)
    nombre = models.CharField(max_length=250)
    contrato = models.CharField(max_length=50)

    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    concepto = models.ForeignKey(
        "ConceptoNomina",
        on_delete=models.PROTECT,
        related_name="novedades"
    )

    valor = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    descuenta_sueldo = models.BooleanField(default=False)
    dias = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "nomina_novedades"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.cedula} - {self.valor}"
    
    
    

# modeles de nomina_cargue.html

from django.db import models
from django.utils import timezone

# Ajusta el import según donde tengas ConceptoNomina
# from myapp.models import ConceptoNomina


class Nomina(models.Model):
    """
    Encabezado: aquí van fechas y consecutivo.
    """
    consecutivo = models.CharField(max_length=20, unique=True, blank=True, default="")
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # Consecutivo basado en ID (sin tabla extra)
        if is_new and not self.consecutivo:
            self.consecutivo = str(self.pk).zfill(6)  # 000001
            super().save(update_fields=["consecutivo"])

    def __str__(self):
        return f"Nómina {self.consecutivo} ({self.fecha_ini} a {self.fecha_fin})"


class NominaEmpleado(models.Model):
    """
    Detalle por empleado dentro de una nómina.
    """
    nomina = models.ForeignKey(Nomina, on_delete=models.CASCADE, related_name="empleados")

    emp_id = models.IntegerField(null=True, blank=True)  # opcional (tu e.id)
    contrato = models.CharField(max_length=50, blank=True, default="")
    cedula = models.CharField(max_length=30, db_index=True)
    nombre = models.CharField(max_length=255, blank=True, default="")
    cargo = models.CharField(max_length=255, blank=True, default="")
    tipo_nomina = models.CharField(max_length=255, blank=True, default="")
    tipo_contrato = models.CharField(max_length=255, blank=True, default="")
    area = models.CharField(max_length=255, blank=True, default="")

    sueldo_base = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    dias_laborados = models.IntegerField(default=0)

    total_salario = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_deducciones = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    total_pagar = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cedula} - {self.nombre}"


class NominaMovimiento(models.Model):
    """
    Movimientos por concepto: NORMALIZADO (no depende de columnas variables).
    """
    nomina = models.ForeignKey(Nomina, on_delete=models.CASCADE, related_name="movimientos")
    nomina_empleado = models.ForeignKey(NominaEmpleado, on_delete=models.CASCADE, related_name="movimientos")

    # Si ConceptoNomina está en tu app, usa ForeignKey real:
    concepto = models.ForeignKey("ConceptoNomina", on_delete=models.PROTECT)

    # devengos/deducciones/carga (lo guardamos para orden/pivot)
    tipo = models.CharField(max_length=20)

    valor = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        indexes = [
            models.Index(fields=["nomina", "nomina_empleado"]),
            models.Index(fields=["nomina", "concepto"]),
        ]




# modelo de pago_nomina.html
from django.db import models


class NominaPago(models.Model):
    nomina = models.ForeignKey(
        "Nomina",
        on_delete=models.CASCADE,
        related_name="pagos_nomina"
    )
    nomina_empleado = models.ForeignKey(
        "NominaEmpleado",
        on_delete=models.CASCADE,
        related_name="pagos_nomina"
    )

    consecutivo_nomina = models.CharField(max_length=20, db_index=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    contrato = models.CharField(max_length=50, blank=True, default="")
    cedula = models.CharField(max_length=30, db_index=True)
    nombre = models.CharField(max_length=255, blank=True, default="")
    tipo_nomina = models.CharField(max_length=255, blank=True, default="")
    tipo_contrato = models.CharField(max_length=255, blank=True, default="")
    cargo = models.CharField(max_length=255, blank=True, default="")
    area = models.CharField(max_length=255, blank=True, default="")

    valor_pagar = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    pago = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    medio_pago = models.CharField(max_length=50, blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "myapp_nominapago"
        constraints = [
            models.UniqueConstraint(
                fields=["nomina", "nomina_empleado"],
                name="uq_nominapago_nomina_empleado"
            )
        ]

    def __str__(self):
        return f"{self.consecutivo_nomina} - {self.cedula} - {self.nombre}"
    


# modelo de parametros_desprendibles.html


class ParametroDesprendibleNomina(models.Model):
    nombre_empresa = models.CharField(max_length=200, blank=True, default="")
    nit = models.CharField(max_length=50, blank=True, default="")
    telefono = models.CharField(max_length=50, blank=True, default="")
    correo_electronico = models.CharField(max_length=150, blank=True, default="")
    direccion = models.CharField(max_length=250, blank=True, default="")
    pagina_web = models.CharField(max_length=200, blank=True, default="")
    logo = models.ImageField(upload_to="logos_desprendibles/", blank=True, null=True)

    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Parámetro de desprendible de nómina"
        verbose_name_plural = "Parámetros de desprendibles de nómina"

    def __str__(self):
        return "Parámetros de desprendible de nómina"




# modelo de formulario_contable.html

from django.db import models


class empresa_contable(models.Model):
    nombre_empresa = models.CharField(max_length=200, blank=True, default='')
    nit = models.CharField(max_length=50, blank=True, default='')
    tel1 = models.CharField(max_length=50, blank=True, default='')
    tel2 = models.CharField(max_length=50, blank=True, default='')
    direccion = models.CharField(max_length=250, blank=True, default='')
    sitio_web = models.CharField(max_length=250, blank=True, default='')
    correo_notificaciones = models.EmailField(blank=True, default='')

    regimen_tributario = models.CharField(max_length=100, blank=True, default='')
    regimen_ica = models.CharField(max_length=100, blank=True, default='')

    camara_comercio = models.CharField(max_length=200, blank=True, default='')
    logo = models.ImageField(upload_to='logos_contabilidad/', blank=True, null=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'empresa contable'
        verbose_name_plural = 'empresa contable'

    def __str__(self):
        return self.nombre_empresa or 'configuracion contable'


class sucursal_contable(models.Model):
    empresa = models.ForeignKey(
        empresa_contable,
        on_delete=models.CASCADE,
        related_name='sucursales'
    )
    numero = models.CharField(max_length=50, blank=True, default='')
    nombre = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        verbose_name = 'sucursal contable'
        verbose_name_plural = 'sucursales contables'
        ordering = ['id']

    def __str__(self):
        return f'{self.numero} - {self.nombre}'

