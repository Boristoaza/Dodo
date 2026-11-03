
from django.urls import path
from . import views

app_name = "proveedores"

urlpatterns = [
    path('proveedores/',views.proveedores_view,name="proveedores")
]