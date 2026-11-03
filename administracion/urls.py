from django.urls import path
from . import views

app_name = 'administracion'

urlpatterns = [
    path('administracion/', views.administracion_view, name='administracion'),
    # path('empresas/', views.empresas_view, name='empresas'),
    # path('sucursales/', views.sucursales_view, name='sucursales'),
    # path('empleados/', views.empleados_view, name='empleados'),
]