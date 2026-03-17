from django.contrib import admin
from django.contrib import admin
from .models import FacturaVenta, FacturaVentaLinea

# Register your models here.

admin.site.register(FacturaVenta)
admin.site.register(FacturaVentaLinea)
