


from .models import InterfazSistema, PermisoInterfazUsuario


def usuario_es_superadmin(user):
    return user.is_authenticated and user.is_superuser


def usuario_es_admin_empresa(user):
    return (
        user.is_authenticated
        and hasattr(user, "perfil")
        and user.perfil.es_administrador_empresa
    )


def puede_entrar_interfaz(user, codigo_interfaz):
    """
    Reglas:
    - superadmin: entra a todo
    - admin empresa: entra a todo dentro de su empresa
    - usuario normal: depende de puede_consultar
    """

    if not user.is_authenticated:
        return False

    if usuario_es_superadmin(user):
        return True

    if usuario_es_admin_empresa(user):
        return True

    if not hasattr(user, "perfil"):
        return False

    try:
        interfaz = InterfazSistema.objects.get(codigo=codigo_interfaz, activa=True)
    except InterfazSistema.DoesNotExist:
        return False

    return PermisoInterfazUsuario.objects.filter(
        perfil=user.perfil,
        interfaz=interfaz,
        puede_consultar=True
    ).exists()


def obtener_permiso_interfaz(user, codigo_interfaz):
    permiso_base = {
        "consultar": False,
        "crear": False,
        "modificar": False,
        "eliminar": False,
    }

    if not user.is_authenticated:
        return permiso_base

    if usuario_es_superadmin(user) or usuario_es_admin_empresa(user):
        return {
            "consultar": True,
            "crear": True,
            "modificar": True,
            "eliminar": True,
        }

    if not hasattr(user, "perfil"):
        return permiso_base

    try:
        interfaz = InterfazSistema.objects.get(codigo=codigo_interfaz, activa=True)
    except InterfazSistema.DoesNotExist:
        return permiso_base

    permiso = PermisoInterfazUsuario.objects.filter(
        perfil=user.perfil,
        interfaz=interfaz
    ).first()

    if not permiso:
        return permiso_base

    return {
        "consultar": permiso.puede_consultar,
        "crear": permiso.puede_crear,
        "modificar": permiso.puede_modificar,
        "eliminar": permiso.puede_eliminar,
    }


