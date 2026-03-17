

from functools import wraps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .permisos import puede_entrar_interfaz



from functools import wraps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .permisos import puede_entrar_interfaz


def permiso_interfaz_requerido(codigo_interfaz):
    def decorator(view_func):
        @login_required(login_url="login")
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if puede_entrar_interfaz(request.user, codigo_interfaz):
                return view_func(request, *args, **kwargs)

            return HttpResponse(
                "<h2 style='font-family:Arial; color:#b91c1c;'>❌ No tienes permisos para acceder a esta sección.</h2>",
                status=403
            )
        return _wrapped_view
    return decorator