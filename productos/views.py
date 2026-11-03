from django.shortcuts import render
from .models import Producto,Lote

def productos(request):
    return render(request,'productos.html')

def registrar_productos(request):
    return render(request,'forms/registrar_productos.html')

def listar_productos(request):
    productos = Producto.objects.prefetch_related('lotes').all()

    contexto = {
        'productos': productos
    }

    return render(request, 'listar_productos.html', contexto)