from django.urls import path
from . import views

app_name = "ventas"

urlpatterns = [
    path('punto_ventas/',views.punto_venta_view,name='punto_venta')
]