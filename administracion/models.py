from django.db import models

# Create your models here.
class Dojo(models.Model):
    """Registra el listado de Dojos"""

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    Poblacion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return(self.nombre)


class Alumno(models.Model):
    """Listados de alumnos"""
    
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    grado = models.IntegerField(blank=True, null=True)
    instructor = models.BooleanField(default=False)
    renshi = models.DateField(auto_now=False, auto_now_add=False, blank = True, null = True)
    kyoshi = models.DateField(auto_now=False, auto_now_add=False, blank = True, null = True)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ['apellidos', 'nombre']
    
    def __str__(self):
        return '{}, {}. {}'.format(self.apellidos, self.nombre, self.grado)


class Cursillo(models.Model):
    """Listado de los cursillos"""
    
    evento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50, default='España')
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    examenes = models.BooleanField()
    alumnos = models.ManyToManyField(Alumno)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return '{} - {}'.format(self.fecha, self.evento)


class Examen(models.Model):
    """Realización de exámenes"""
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    evento = models.ForeignKey(Cursillo, on_delete=models.CASCADE)
    grado = models.IntegerField()

    class Meta:
        verbose_name_plural = "Examenes"
        ordering = ['grado']

    def __str__(self):
        return '{} - {}'.format(self.alumno, self.grado)