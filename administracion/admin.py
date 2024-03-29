from django.contrib import admin

from .models import *


class ExamenAdmin(admin.ModelAdmin):
    list_display = ('evento', 'alumno', 'grado')
    raw_id_fields = ('alumno',)
    list_filter = ('evento',)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'correo', 'telefono', 'grado')


class DojoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'nombre_instructor',
                    'apellidos_instructor')


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'dojo', 'fecha_nacimiento', 'grado', 'activo')
    list_filter = ('dojo',)
    raw_id_fields = ('dojo',)
    search_fields = ('nombre', 'apellidos')


class CursilloAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'evento', 'ciudad', 'pais', 'internacional')
    list_filter = ('ciudad', 'pais', 'internacional')
    date_hierarchy = 'fecha'
    filter_horizontal = ('alumnos',)


class PeticionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'dojo', 'titulo', 'finalizada')
    list_filter = ('dojo', 'finalizada')


# Register your models here.

admin.site.site_header = 'Panel de control OGKKE'
admin.site.index_title = 'Administración OGKKE'
admin.site.site_title = 'Admin OGKKE'

admin.site.register(Dojo, DojoAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Cursillo, CursilloAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Peticion, PeticionAdmin)
admin.site.register(Instructor, InstructorAdmin)
