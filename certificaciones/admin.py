from django.contrib import admin
from .models import Certificaciones
# Register your models here.

class CertificacionesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Certificaciones,CertificacionesAdmin)