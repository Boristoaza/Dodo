from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')

        obtener_username = User.objects.filter(email=correo).values_list('username',flat=True).first()
        if obtener_username:
          user = authenticate(request, username=obtener_username, password=contrasenia)
          if user is not None:
                print(user)
                login(request, user)
                if request.user.is_authenticated:
                 return redirect('core:main')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')

def error_404_view(request):
    return render(request, '404.html', status=404)