from django.shortcuts import render,HttpResponse

# Create your views here.
def hola(req):
    return render(req,"proyecto/home.html",{"hola":["asdas","Adsa"]})

