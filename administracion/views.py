from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from administracion.models import Dojo

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

def login_view(request):
    """Vista para login en aplicación"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'Usuario y/o password incorrecto'})

    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def alumnos_view(request):
    return render(request, 'alumnos.html')


class DojosView(LoginRequiredMixin, ListView):
    """Listado de gimnasios de la asociación"""
    template_name = 'dojos.html'
    model = Dojo
    context_object_name = 'dojo'