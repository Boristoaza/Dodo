from django.urls import path
from . import views


app_name="empresas"

urlpatterns = [
    path('empresas/',views.empresas_view , name="empresas"),
    path('registrar_empresa/',views.registrar_empresa_view , name="registrar_empresa" )
]