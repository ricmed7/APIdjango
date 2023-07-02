from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Consulta
from .serializer import ConsultaSerielizer

@api_view(['GET','POST'])
def consulta_api_view(request):

  if request.method=='GET':
    listaconsulta=Consulta.objects.all()
    consulta_serializer=ConsultaSerielizer(listaconsulta,many=True)
    return Response(consulta_serializer.data, status=status.HTTP_200_OK)
  
  elif request.method=='POST':
    consulta_serializer=ConsultaSerielizer(data=request.data)
    if consulta_serializer.is_valid():
      consulta_serializer.save()
      return Response(consulta_serializer.data, status=status.HTTP_201_CREATED)
    return Response(consulta_serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
 
@api_view(['GET','PUT','DELETE'])
def consulta_detalle_view(request,consulta_id=None):
  consulta=Consulta.objects.filter(id=consulta_id).first()
  if consulta:
    if request.method=='GET':
      consulta_serializer=ConsultaSerielizer(consulta)
      return Response(consulta_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
      request.data
      consulta_serializer=ConsultaSerielizer(consulta,data=request.data)
      if consulta_serializer.is_valid():
        consulta_serializer.save()
        return Response(consulta_serializer.data, status=status.HTTP_200_OK)
      return Response(consulta_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
      consulta.delete()
      return Response({'message':'Eliminado correctamente!'}, status=status.HTTP_200_OK)  
  return Response({'message':'No existe tal registro!'}, status=status.HTTP_400_BAD_REQUEST)  
