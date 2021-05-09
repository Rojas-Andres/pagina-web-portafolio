from django.shortcuts import render
from proyectos.models import Proyectos

# Create your views here.

def proyectos(req):
    proyectos = Proyectos.objects.all() # Traiga todos los servicios que esten creados
    print(proyectos)
    return render(req,"proyectos/proyectos.html",{"proyectos":proyectos})