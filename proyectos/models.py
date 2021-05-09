from django.db import models

# Create your models here.

class Proyectos(models.Model):
    nombre         = models.CharField(max_length=50)
    url            = models.URLField(max_length = 200)
    contenido      = models.CharField(max_length=200)
    imagen         = models.ImageField(upload_to="proyectos",null=True,blank=True)
    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural="Proyectos"