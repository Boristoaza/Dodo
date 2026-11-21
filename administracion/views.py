from django.shortcuts import render

# Create your views here.
def administracion_view(request):
    return render(request,'views/administracion.html')

def crear_cliente(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa')
        ruc = request.POST.get('ruc')
        correo_empresa = request.POST.get('correo_empresa')
        telefono_empresa = request.POST.get('telefono_empresa')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('nombre_empresa')
        actividad = request.POST.get('actividad')

        print(nombre_empresa,ruc,correo_empresa,telefono_empresa,ciudad,direccion,actividad)


    return render(request,'forms/registrar_cliente.html')