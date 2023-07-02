from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Especie
from .serializer import EspecieSerielizer

@api_view(['GET','POST'])
def especie_api_view(request):

  if request.method=='GET':
    listaespecie=Especie.objects.all()
    especie_serializer=EspecieSerielizer(listaespecie,many=True)
    return Response(especie_serializer.data, status=status.HTTP_200_OK)
  
  elif request.method=='POST':
    especie_serializer=EspecieSerielizer(data=request.data)
    if especie_serializer.is_valid():
      especie_serializer.save()
      return Response(especie_serializer.data, status=status.HTTP_201_CREATED)
    return Response(especie_serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
 
@api_view(['GET','PUT','DELETE'])
def especie_detalle_view(request,especie_id=None):
  especie=Especie.objects.filter(id=especie_id).first()
  if especie:
    if request.method=='GET':
      especie_serializer=EspecieSerielizer(especie)
      return Response(especie_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
      request.data
      especie_serializer=EspecieSerielizer(especie,data=request.data)
      if especie_serializer.is_valid():
        especie_serializer.save()
        return Response(especie_serializer.data, status=status.HTTP_200_OK)
      return Response(especie_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
      especie.delete()
      return Response({'message':'Eliminado correctamente!'}, status=status.HTTP_200_OK)  
  return Response({'message':'No existe tal registro!'}, status=status.HTTP_400_BAD_REQUEST)  
