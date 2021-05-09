
from django.contrib import admin
from django.urls import path
from certificaciones import views
urlpatterns = [
    path('', views.certificaciones,name="Certificaciones"),
]
