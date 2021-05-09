from django.shortcuts import render
from .models import Certificaciones
# Create your views here.
def certificaciones(req):
    certificaciones = Certificaciones.objects.all()
    return render(req,"certificaciones/certificaciones.html",{"certificaciones":certificaciones})