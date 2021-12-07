"""karateclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from administracion import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('alumnos/', views.alumnos_view, name='alumnos'),
    path('alumnos/<int:grado>/', views.alumnos_view, name='alumnosdan'),
    path('alumnos/<int:grado>/<int:id>',
         views.alumnos_detalle_view, name='alumnosdetalle'),
    path('buscar/', views.buscar_view, name='buscar'),
    path('dojos/', views.DojosView.as_view(), name='dojos'),
    path('dojos/<int:dojo>/', views.DojoDetail, name='dojodetail'),
    path('cursillos/', views.cursillos_view, name='cursillos'),
    path('cursillos/<int:cursillo>/', views.cursillo_detalle, name='cursillo'),
    path('cursillos/<int:cursillo>/examen',
         views.cursillo_examen, name='examen'),
    path('cursillos/inscripcion/', views.cursillo_inscripcion, name='inscripcion'),
    path('peticion/', views.peticion_view, name='peticion'),
    path('admin/', admin.site.urls),
    path('correo/', views.correo_view, name='correo'),
    path('correo/correo-enviado', views.correo_enviado_view, name='correo-enviado'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
