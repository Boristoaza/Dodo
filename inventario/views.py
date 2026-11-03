from django.shortcuts import render

# Create your views here.
def inventario_view(request):
    return render(request,'inventario.html')