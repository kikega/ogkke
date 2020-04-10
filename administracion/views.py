from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request, 'base.html')

def login_view(request):
    """Vista para login en aplicación"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('administracion.administracion')
        else:
            return render(request, 'login.html', {'error':'Usuario y/o password incorrecto'})

    return render(request, 'login.html')
