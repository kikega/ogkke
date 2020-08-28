from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from administracion.models import Dojo, Alumno, Examen, Cursillo, Peticion

# Create your views here.

@login_required
def index(request):
    """Página principal de la aplicación, nos mostrará un resúmen con datos globales"""
    cn = Alumno.objects.all().count()
    cursos = Cursillo.objects.all().count()
    nacional = Cursillo.objects.filter(pais='España').count()
    int = Cursillo.objects.filter(internacional=True).count()
    extranjero = Cursillo.objects.exclude(pais='España').count()
    peticiones = Peticion.objects.filter(finalizada=False).count()
    dojos = Dojo.objects.all().count()
    danes = list()
    for i in range(1, 9):
        i = Alumno.objects.filter(grado=i).count()
        danes.append(i)
    return render(request, 'index.html', {
        'cn':cn, 
        'danes':danes, 
        'cursos':cursos, 
        'nacional':nacional, 
        'int':int,
        'extranjero':extranjero,
        'peticiones':peticiones,
        'dojos':dojos,
        })


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


@login_required
def buscar_view(request):
    """Buscamos un cinto negro por su apellido"""
    error = []
    if request.method == 'POST':
        if not request.POST.get('apellido', ""):
            error.append('Debes introducir el apellido de una persona')
        apellido = request.POST['apellido']
        alumno = Alumno.objects.filter(apellidos__icontains=request.POST['apellido'])
        cantidad = Alumno.objects.filter(apellidos__icontains=request.POST['apellido']).count()

    return render(request, 'busqueda.html', {'alumno':alumno, 'cantidad':cantidad, 'error':error})


@login_required
def peticion_view(request):
    if request.method == 'POST':
        p = Peticion()
        p.titulo = request.POST['titulo']
        p.tipo = request.POST['tipo']
        p.descripcion = request.POST['descripcion']
        dojo = request.POST['dojo']
        d = Dojo.objects.get(pk=dojo)
        p.dojo = Dojo()
        p.dojo = d
        p.save()

    peticion = Peticion.objects.filter(finalizada=False)
    cantidad = Peticion.objects.filter(finalizada=False).count()

    return render(request, 'peticion.html', {'peticion':peticion, 'cantidad':cantidad})


class DojosView(LoginRequiredMixin, ListView):
    """Listado de gimnasios de la asociación"""
    template_name = 'dojos.html'
    model = Dojo
    context_object_name = 'dojo'


@login_required
def DojoDetail(request, dojo):
    danes = list()
    gym = Dojo.objects.get(id=dojo)
    alumno = Alumno.objects.filter(dojo=dojo).order_by('-grado','apellidos')
    cantidad = Alumno.objects.filter(dojo=dojo).count()
    for i in range(1, 9):
        i = Alumno.objects.filter(dojo=dojo,grado=i).count()
        danes.append(i)
    return render(request, 'dojodetail.html', {'dojo':gym, 'alumno':alumno, 'cantidad':cantidad, 'danes':danes})


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


@login_required
def cursillo_detalle(request, cursillo):
    curso = Cursillo.objects.get(id=cursillo)
    examenes = Examen.objects.filter(evento=cursillo)
    return render(request, 'cursillodetalle.html', {'curso':curso, 'examenes':examenes})
