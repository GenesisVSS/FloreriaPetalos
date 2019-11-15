from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home_admin/',home_admin,name='home_admin'),
    path('home_usu/',home_usu,name='home_usu'),
    path('galeria_admin/',galeria_admin,name='galeria_admin'),
    path('galeria_usu/',galeria_usu,name='galeria_usu'),
    path('formulario/',formulario,name='formulario'),
    path('eliminar_flor/<id>/',eliminar_flor,name='eliminar'),
    path('login_inicio/',login_inicio,name='login_inicio'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('',login,name='login'),
]