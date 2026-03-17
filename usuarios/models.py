from django.db import models




from django.contrib.auth.models import User


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.nit}"


class PerfilUsuario(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil"
    )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="usuarios",
        blank=True,
        null=True
    )
    nombre_completo = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    es_administrador_empresa = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuario"
        ordering = ["user__username"]

    def __str__(self):
        if self.empresa:
            return f"{self.user.username} - {self.empresa.nombre}"
        return f"{self.user.username} - Sin empresa"


class InterfazSistema(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=150)
    modulo = models.CharField(max_length=100, blank=True, null=True)
    template = models.CharField(max_length=200, blank=True, null=True)
    url_name = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Interfaz del sistema"
        verbose_name_plural = "Interfaces del sistema"
        ordering = ["modulo", "nombre"]

    def __str__(self):
        return f"{self.modulo or 'General'} - {self.nombre}"


class PermisoInterfazUsuario(models.Model):
    perfil = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.CASCADE,
        related_name="permisos_interfaz"
    )
    interfaz = models.ForeignKey(
        InterfazSistema,
        on_delete=models.CASCADE,
        related_name="permisos_usuario"
    )

    puede_consultar = models.BooleanField(default=False)
    puede_crear = models.BooleanField(default=False)
    puede_modificar = models.BooleanField(default=False)
    puede_eliminar = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Permiso por interfaz"
        verbose_name_plural = "Permisos por interfaz"
        unique_together = ("perfil", "interfaz")
        ordering = ["perfil__user__username", "interfaz__modulo", "interfaz__nombre"]

    def __str__(self):
        return f"{self.perfil.user.username} - {self.interfaz.codigo}"