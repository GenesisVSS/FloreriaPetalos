from django.shortcuts import render
from .models import Flores 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/principal_login/')
def home(request):
    return render(request,'core/home.html')

def galeria(request):
    flores=Flores.objects.all()
    return render(request,'core/galeria.html',{'listaFlores':flores})
def formulario(request):
    florr=Flores.objects.all()
    if request.POST:
        Name=request.POST.get("txtNombre")
        Valor=request.POST.get("txtValor")
        Descripcion=request.POST.get("txtDesc")
        Estado=request.POST.get("txtEstado")
        Stock=request.POST.get("txtStock")
        Imagen=request.FILES.get("txtImagen")
        flor=Flores(
            name=Name,
            valor=Valor,
            descripcion=Descripcion,
            estado=Estado,
            stock=Stock,
            imagen=Imagen
        )
        flor.save() #graba el objeto e bdd
        return render(request,'core/formulario.html',{'lista':florr,'msg':'grabo','sw':True})
    return render(request,'core/formulario.html',{'lista':florr})#pasan los datos a la web

def eliminar_flor(request,id): 
    flor=Flores.objects.get(name=id)
    flor.delete()
        
    return HttpResponse("<script> ;window.location.href='/galeria/';</script>")

def principal_login(request):
    return render(request,'core/principal_login.html')

def login_inicio(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        c=request.POST.get("txtPassword")
        usu=authenticate(request,username=u,password=c)
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request,'core/home.html')
    return render(request,'core/principal_login.html')

def login_admin(request):
    return render(request,'core/login_admin.html')

def login_usuario(request):
    return render(request,'core/login_usuario.html')

def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>alert('cerro sesion');window.location.href='/';</script>")


        


