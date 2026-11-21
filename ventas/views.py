from django.shortcuts import render
from productos.models import Producto
# Create your views here.
def punto_venta_view(request):

    productos = Producto.objects.values()

    print(productos)

    contexto = {'productos':productos}
    
    return render(request,'punto_ventas.html', contexto)