from django.shortcuts import render

# Create your views here.
def empresas_view(request):
    return render(request,'empresa.html')