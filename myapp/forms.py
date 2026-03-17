

from django import forms
from .models import Tercero
from .models import CuentaContable
from django import forms
from django.forms import modelformset_factory
from .models import DocumentoContable
from .models import AsientoContable




class TerceroForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = '__all__'



class CuentaContableForm(forms.ModelForm):
    class Meta:
        model = CuentaContable
        # Excluimos campos calculados
        exclude = ['nivel', 'padre']
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'p.ej. 110202'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'p.ej. Bancos nacionales'}),
        }
        labels = {
            'codigo': 'Código contable',
            'nombre': 'Cuenta contable',
            'movimiento': 'Movimiento',
            'centro_costo': 'Centro de costo',
            'criterio1': 'Criterio 1',
            'criterio2': 'Criterio 2',
            'criterio3': 'Criterio 3',
        }

#___________________________insertar archivo csv

class CuentasUploadForm(forms.Form):
    MODO_CHOICES = [
        ('insert', 'Solo insertar (omite repetidos)'),
        ('upsert', 'Insertar o actualizar (si ya existe, actualiza)'),
    ]
    archivo = forms.FileField(help_text="Archivo CSV con encabezados: codigo,nombre,movimiento,centro_costo,criterio1,criterio2,criterio3")
    modo = forms.ChoiceField(choices=MODO_CHOICES, initial='upsert')



#_______________________formulario para crear documentos contables

class DocumentoContableForm(forms.ModelForm):
    class Meta:
        model = DocumentoContable
        fields = ['codigo', 'nombre']
        labels = {'codigo': 'Código del documento', 'nombre': 'Nombre del documento'}
        widgets = {
            'codigo': forms.TextInput(attrs={'placeholder': 'Ej: RC, FC001, AJ-01'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Recibo de caja'}),
        }

# El formset lo crearemos en la vista para poder ajustar extra y can_delete

class AsientoForm(forms.ModelForm):
    class Meta:
        model = AsientoContable
        fields = ['fecha', 'documento', 'descripcion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

        



