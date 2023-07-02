from rest_framework import serializers
from .models import Propietario,Especie,Mascota,Consulta
#importando el modelo user de django
from django.contrib.auth.models import User


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Propietario
        #indicandole que campos van a ser serializados
        #fields=('nombres','apellidos','ci')
        #indicando que todos los campos se tomen encuenta
        fields='__all__'

class EspecieSerielizer(serializers.ModelSerializer):
    class Meta:
        model=Especie
        fields='__all__'

class MascotaSerielizer(serializers.ModelSerializer):
    class Meta:
        model=Mascota
        fields='__all__'

class ConsultaSerielizer(serializers.ModelSerializer):
    class Meta:
        model=Consulta
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        #fields='__all__'
        fields=('id','username','password')
    #esta funcion encripta el password
    def create(self, validate_data):
        user=User(**validate_data)
        user.set_password(validate_data['password'])    
        user.save()
        return user
    def update(self,instance,validated_data):
        update_user=super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


