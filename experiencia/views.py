from django.shortcuts import render
from experiencia.models import Experiencia
# Create your views here.
def experiencia(req):

    experiencias = Experiencia.objects.all()
    return render(req,"experiencia/experiencia.html",{"experiencias":experiencias})