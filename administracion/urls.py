from django.urls import path

from administracion import views

app_name = 'administracion'

urlpatterns = [
    path('', views.index, name='administracion'),
]