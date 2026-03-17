
from django.contrib import admin
from django.urls import path, include
from usuarios import views as user_views  # vistas de autenticación

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticación
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),

    # Incluimos todas las rutas de la app principal
    path('', include('myapp.urls')),
]