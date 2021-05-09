from django.shortcuts import render,HttpResponse

# Create your views here.
def hola(req):
    return render(req,"proyecto/home.html",{"hola":["asdas","Adsa"]})
def contacto(req):
    return render(req,"proyecto/contacto.html",{"hola":["asdas","Adsa"]})

def proyectos(req):
    return render(req,"proyecto/proyectos.html",{"hola":["asdas","Adsa"]})
def experiencia(req):
    return render(req,"proyecto/experiencia.html",{"hola":["asdas","Adsa"]})