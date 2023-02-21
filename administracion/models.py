from django.db import models

# Create your models here.


class Instructor(models.Model):
    """Tabla para el registro de instructores"""
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    grado = models.IntegerField(blank=True, null=True)
    RANGO_GRADO = (
        ('h', 'Hanshi'),
        ('r', 'Renshi'),
        ('k', 'Kyoshi'),
    )
    rango = models.CharField(
        max_length=1, choices=RANGO_GRADO, blank=True, null=True)
    foto = models.ImageField(upload_to='administracion', blank=True, null=True)


class Dojo(models.Model):
    """Registra el listado de Dojos"""

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    Poblacion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    correo = models.EmailField(max_length=254, blank=True, null=True)
    nombre_instructor = models.CharField(max_length=50, blank=True, null=True)
    apellidos_instructor = models.CharField(
        max_length=50, blank=True, null=True)
    grado = models.IntegerField(blank=True, null=True)
    RANGO_GRADO = (
        ('h', 'Hanshi'),
        ('r', 'Renshi'),
        ('k', 'Kyoshi'),
    )
    rango = models.CharField(
        max_length=1, choices=RANGO_GRADO, blank=True, null=True)
    foto_instructor = models.ImageField(
        upload_to='administracion', blank=True, null=True)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return(self.nombre)


class Alumno(models.Model):
    """Listados de alumnos"""

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    grado = models.IntegerField(blank=True, null=True)
    renshi = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    kyoshi = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
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
    internacional = models.BooleanField(default=False, blank=True)
    pais = models.CharField(max_length=50, default='España')
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    examenes = models.BooleanField()
    alumnos = models.ManyToManyField(Alumno, blank=True, null=True)

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


class Peticion(models.Model):

    fecha = models.DateField(auto_now=False, auto_now_add=True)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    TIPO_PETICION = (
        ('a', 'Añadir'),
        ('m', 'Modificar'),
        ('e', 'Eliminar'),
    )
    titulo = models.CharField(max_length=550)
    tipo = models.CharField(
        max_length=1, choices=TIPO_PETICION, blank=True, null=True)
    descripcion = models.TextField()
    finalizada = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Peticion")
        verbose_name_plural = ("Peticiones")
        ordering = ['dojo', 'fecha']

    def __str__(self):
        return '{}: {} - {}'.format(self.fecha, self.titulo, self.finalizada)
