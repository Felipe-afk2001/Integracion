from core.forms import user_form
from django.db import models
from .models import autor
from .models import obras as Obras
from .models import categorias
from django.shortcuts import redirect, render
from adminapp.models import usuarios

# Create your views here.
def index(request):
    categoria=categorias.objects.all()
    contexto={
        'categoria':categoria
    }
    return render(request,'core/index.html', contexto)

def obras(request,id):
    obra=Obras.objects.get(id_obra=id)
    contexto = {
        'obra':obra
    }
    return render(request,'core/obras.html',contexto)

def autores(request):
    autores=autor.objects.all()
    contexto={
        'autores':autores
    }
    return render(request,'core/autores.html',contexto)

def login(request):
    return render(request,'core/Iniciar_sesion.html')

def chicagogaleria(request):
    return render(request,'core/chicagogaleria.html')

def Autor(request,id):
    obra=Obras.objects.filter(autor=id)
    Autor=autor.objects.get(id_autor=id)
    contexto={
        'autor':Autor,
        'obras':obra
    }
    return render(request,'core/autor.html',contexto)  


def categoria(request,id):
    Autor=autor.objects.filter(categorias=id)
    nom=''
    contexto= {
        'autores':Autor,'nom':nom
    }
    return render(request,'core/categorias.html',contexto)

def load(request):
    return render(request,'core/load.html')    

def registrarse (request):
    msg3= ''
    formulario3= user_form()
    if request.method == 'POST':
        formulario3=user_form(request.POST)
        if formulario3.is_valid():
            formulario3.save()
            msg3='El usuario se registro correctamente'
        else:
            msg3='El usuario ya existe'
    contexto = {
        'formulario3':formulario3, 'msg3':msg3, 
    }
    return render(request,'core/Registrarse.html',contexto)
     