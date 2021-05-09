from django.db import models

# Create your models here.

class Certificaciones(models.Model):
    nombre         = models.CharField(max_length=50)
    url            = models.URLField(max_length = 200)
    contenido      = models.TextField()
    imagen         = models.ImageField(upload_to="certificaciones",null=True,blank=True)
    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Certificacion"
        verbose_name_plural="Certificaciones"
    