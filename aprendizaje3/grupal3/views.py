from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': lista_usuarios})