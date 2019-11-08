from django.shortcuts import render
from .models import Flores 

# Create your views here.
def home(request):
    return render(request,'core/home.html')
def galeria(request):
    flores=Flores.objects.all()
    return render(request,'core/galeria.html',{'listaFlores':flores})
def formulario(request):
    florr=Flores.objects.all()# select * from Categoria
    if request.POST:
        Name=request.POST.get("txtNombre")
        Valor=request.POST.get("txtValor")
        Descripcion=request.POST.get("txtDesc")
        Estado=request.POST.get("txtEstado")
        Stock=request.POST.get("txtStock")
        #recuperar la imagen desde el formulario
        Imagen=request.FILES.get("txtImagen")
        #crear una instancia de Pelicula (modelo)
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
