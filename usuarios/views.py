from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('email')
        contrasenia = request.POST.get('contrasenia')

        user = authenticate(request, username=usuario, password=contrasenia)

        if user is not None:
            login(request, user)
            return redirect('core:home')

    return render(request, 'login.html')


@login_required
def perfil_view(request):
    return render(request, 'perfil.html')