from django.shortcuts import render

# Create your views here.
def punto_venta_view(request):
    return render(request,'punto_ventas.html')