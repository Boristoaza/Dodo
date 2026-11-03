from django.urls import path
from . import views

app_name="compras"

urlpatterns = [
    path('compras/',views.compras_view,name="compras")
]