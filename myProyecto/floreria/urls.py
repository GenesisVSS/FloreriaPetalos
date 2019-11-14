from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('galeria/',galeria,name='galeria'),
    path('formulario/',formulario,name='formulario'),
    path('eliminar_flor/<id>/',eliminar_flor,name='eliminar'),
    path('login_inicio/',login_inicio,name='login_inicio'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('login/',login,name='login'),
]