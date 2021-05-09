from django.shortcuts import render

# Create your views here.
def certificaciones(req):
    return render(req,"certificaciones/certificaciones.html")