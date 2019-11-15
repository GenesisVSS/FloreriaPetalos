from django.shortcuts import render
from .models import Flores 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required

# CREACION DE VISTAS

def home_admin(request):
    return render(request,'core/home_admin.html')


def home_usu(request):
    return render(request,'core/home_usu.html')


def galeria_admin(request):
    flores=Flores.objects.all()
    #SE TOMAN LAS FLORES QUE SE HAYAN INGRESADO A LA LISTA 
    return render(request,'core/galeria_admin.html',{'listaFlores':flores})


def galeria_usu(request):
    flores=Flores.objects.all()
    #SE TOMAN LAS FLORES QUE SE HAYAN INGRESADO A LA LISTA 
    return render(request,'core/galeria_usu.html',{'listaFlores':flores})

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
        flor.save() #graba el objeto en bdd
        return render(request,'core/formulario.html',{'lista':florr,'msg':'grabo','sw':True})
        #pasa los datos a la web
    return render(request,'core/formulario.html',{'lista':florr})

def eliminar_flor(request,id): 
    flor=Flores.objects.get(name=id)
    flor.delete()
    #SE RETORNA A LA PAGINA QUE SE COLOCA EN EL HREF LUEGO DE REALIZAR LA ACCION
    return HttpResponse("<script> ;window.location.href='/galeria_admin/';</script>")

def login_inicio(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        c=request.POST.get("txtPassword")
        #VALIDACION DEL USUARIO
        usu=authenticate(request,username=u,password=c)
        if usu is not None and usu.is_active:
            if usu.is_staff:
                auth_login(request, usu)
                arreglo={'nombre':u, 'contrasena':c, 'tipo':'administrador'}
                return render(request,'core/home_admin.html',arreglo)
            else:
                arreglo={'nombre':u, 'contrasena':c, 'tipo':'cliente'}
                return render(request,'core/home_usu.html',arreglo)
        variables={
            'msg':'no existe nada'
        }
    return render(request,'core/login.html',variables)

def login(request):
    return render(request,'core/login.html')

def cerrar_sesion(request):
    logout(request)
    return HttpResponse("<script>;window.location.href='/';</script>")


        


