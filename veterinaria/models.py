from django.db import models


class Propietario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    ci = models.CharField(max_length=15)
    direccion = models.TextField()
    contacto=models.IntegerField()
    correo=models.EmailField()
    #created_at=models.DateField(auto_now_add=True)

class Especie(models.Model):
    nombre=models.CharField(max_length= 50)
    #created_at=models.DateField(auto_now_add=True)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    edad=models.IntegerField()
    #created_at=models.DateField(auto_now_add=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    especie=models.ForeignKey(Especie, on_delete=models.CASCADE)

class Consulta(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    #created_at=models.DateField(auto_now_add=True)
    mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    

# Create your models here.
