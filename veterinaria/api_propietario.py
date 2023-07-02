from rest_framework import status
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Propietario
from .serializer import PropietarioSerializer

@api_view(['GET','POST'])
def propietario_api_view(request):
  if request.method=='GET':
    listapropietarios=Propietario.objects.all()
    propietarios_serializer=PropietarioSerializer(listapropietarios,many=True)
    return Response(propietarios_serializer.data, status=status.HTTP_200_OK)
  
  elif request.method=='POST':
    propietarios_serializer=PropietarioSerializer(data=request.data)
    if propietarios_serializer.is_valid():
      propietarios_serializer.save()
      return Response(propietarios_serializer.data, status=status.HTTP_201_CREATED)
    return Response(propietarios_serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT','DELETE'])
def propietario_detalle_view(request,propietario_id=None):
  propietario=Propietario.objects.filter(id=propietario_id).first()
  if propietario:
    if request.method=='GET':
      #propietario=Propietario.objects.filter(id=propietario_id).first()
      propietario_serializer=PropietarioSerializer(propietario)
      return Response(propietario_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
      request.data
      #propietario=Propietario.objects.filter(id=propietario_id).first()
      propietario_serializer=PropietarioSerializer(propietario,data=request.data)
      if propietario_serializer.is_valid():
        propietario_serializer.save()
        return Response(propietario_serializer.data, status=status.HTTP_200_OK)
      return Response(propietario_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
      #propietario=Propietario.objects.filter(id=propietario_id).first()
      propietario.delete()
      return Response({'message':'Eliminado correctamente!'}, status=status.HTTP_200_OK)  
  return Response({'message':'No existe tal registro!'}, status=status.HTTP_400_BAD_REQUEST)  

