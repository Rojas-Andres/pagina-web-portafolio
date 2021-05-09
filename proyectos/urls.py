
from django.contrib import admin
from django.urls import path
from proyectos import views
urlpatterns = [
    path('', views.proyectos,name="Proyectos"),
]
