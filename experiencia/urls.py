
from django.contrib import admin
from django.urls import path
from experiencia import views
urlpatterns = [
    path('', views.experiencia,name="Experiencia"),
]
