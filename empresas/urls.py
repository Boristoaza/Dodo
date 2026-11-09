from django.urls import path
from . import views

app_name = "empresas"

urlpatterns = [
    path('empresa/', views.empresa_view, name="empresa"),
    # path('registrar_empresa/', views.registrar_empresa_view, name="registrar_empresa"),
    path('sucursal/',views.sucursal_view, name="sucursal"),
    path('listar_empleados/',views.listar_empleados,name='listar_empleados'),
    path('registrar_empleado/', views.registrar_empleados , name="registrar_empleado"),
    path('crear_sucursal/', views.crear_sucursal_view, name="crear_sucursal"),
]