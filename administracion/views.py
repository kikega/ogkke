from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from administracion.models import Dojo, Alumno, Examen, Cursillo

# Create your views here.

@login_required
def index(request):
    """Página principal de la aplicación, nos mostrará un resúmen con datos globales"""
    cn = Alumno.objects.all().count()
    danes = list()
    for i in range(1, 9):
        i = Alumno.objects.filter(grado=i).count()
        danes.append(i)
    return render(request, 'index.html', {'cn':cn, 'danes':danes})

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
    """Vista para hacer logout"""
    logout(request)
    return redirect('login')


@login_required
def alumnos_view(request,grado=1):
    """Listado de los alumnos organizados por el grado"""
    alumno = Alumno.objects.filter(grado=grado).order_by('dojo', 'apellidos')
    cantidad = Alumno.objects.filter(grado=grado).count()
    context = {'grado':grado, 'alumno':alumno, 'cantidad':cantidad}
    return render(request, 'alumnos.html', context)


@login_required
def alumnos_detalle_view(request, grado, id):
    alumno = Alumno.objects.get(id=id)
    examen = Examen.objects.filter(alumno=id)
    return render(request, 'alumnodetalle.html', {'alumno':alumno, 'examen':examen})


class DojosView(LoginRequiredMixin, ListView):
    """Listado de gimnasios de la asociación"""
    template_name = 'dojos.html'
    model = Dojo
    context_object_name = 'dojo'


@login_required
def DojoDetail(request, dojo):
    gym = Dojo.objects.get(id=dojo)
    alumno = Alumno.objects.filter(dojo=dojo).order_by('-grado','apellidos')
    cantidad = Alumno.objects.filter(dojo=dojo).count()
    return render(request, 'dojodetail.html', {'dojo':gym, 'alumno':alumno, 'cantidad':cantidad})


class AlumnosView(LoginRequiredMixin, ListView):
    """Listado de gimnasios de la asociación"""
    template_name = 'alumnos.html'
    model = Alumno
    context_object_name = 'alumnos'


@login_required
def AlumnosDan(request):
    pass


@login_required
def cursillos_view(request):
    cursillo = Cursillo.objects.all()
    return render(request, 'cursillos.html', {'cursillo':cursillo})