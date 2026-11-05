from django.urls import path
from . import views

app_name = "empresas"

urlpatterns = [
    path('empresa/', views.empresa_view, name="empresa"),
    path('sucursal/',views.sucursal_view, name="sucursal"),

    # path('registrar_empresa/', views.registrar_empresa_view, name="registrar_empresa"),
    path('crear_sucursal/', views.crear_sucursal_view, name="crear_sucursal"),
]