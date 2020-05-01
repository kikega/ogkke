from django.contrib import admin

from .models import *

class ExamenAdmin(admin.ModelAdmin):
    list_display = ('evento', 'alumno', 'grado')
    raw_id_fields = ('alumno',)
    list_filter = ('evento',)    


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'dojo', 'grado')
    list_filter = ('dojo',)
    raw_id_fields = ('dojo',)
    search_fields = ('nombre', 'apellidos')

class CursilloAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'evento', 'ciudad')
    list_filter = ('ciudad',)
    date_hierarchy = 'fecha'
    filter_horizontal = ('alumnos',)

# Register your models here.
admin.site.register(Dojo)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Cursillo, CursilloAdmin)
admin.site.register(Examen, ExamenAdmin)
