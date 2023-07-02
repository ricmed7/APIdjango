from django.contrib import admin
from .models import Propietario,Mascota,Especie,Consulta

# Register your models here.
admin.site.register(Propietario)
admin.site.register(Especie)
admin.site.register(Mascota)
admin.site.register(Consulta)
