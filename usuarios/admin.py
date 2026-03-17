from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Empresa, PerfilUsuario, InterfazSistema, PermisoInterfazUsuario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "nit", "telefono", "email", "activa")
    search_fields = ("nombre", "nit")
    list_filter = ("activa",)


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "empresa",
        "nombre_completo",
        "cargo",
        "es_administrador_empresa",
        "activo",
    )
    search_fields = ("user__username", "user__email", "nombre_completo", "empresa__nombre")
    list_filter = ("empresa", "es_administrador_empresa", "activo")


@admin.register(InterfazSistema)
class InterfazSistemaAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo", "nombre", "modulo", "url_name", "activa")
    search_fields = ("codigo", "nombre", "modulo", "url_name", "template")
    list_filter = ("modulo", "activa")


@admin.register(PermisoInterfazUsuario)
class PermisoInterfazUsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "perfil",
        "interfaz",
        "puede_consultar",
        "puede_crear",
        "puede_modificar",
        "puede_eliminar",
    )
    search_fields = (
        "perfil__user__username",
        "perfil__empresa__nombre",
        "interfaz__codigo",
        "interfaz__nombre",
    )
    list_filter = (
        "interfaz__modulo",
        "puede_consultar",
        "puede_crear",
        "puede_modificar",
        "puede_eliminar",
    )