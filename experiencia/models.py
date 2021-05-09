from django.db import models

# Create your models here.


class Experiencia(models.Model):
    empresa    = models.CharField(max_length=50)
    cargo      = models.CharField(max_length = 200)
    contenido  = models.TextField(blank=True)
    imagen     = models.ImageField(upload_to="experiencia",null=True,blank=True)
    inicio     = models.CharField(max_length=50)
    fin        = models.CharField(max_length=50)
    url        = models.URLField(max_length=50)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural="Experiencias"