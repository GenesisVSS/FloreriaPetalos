from django.contrib import admin
from django.urls import path,include
from .views import home,galeria,formulario

urlpatterns = [
    path('',home,name='home'),
    path('galeria/',galeria,name='galeria'),
    path('formulario/',formulario,name='formulario'),
]