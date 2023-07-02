from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import UserSerializer

@api_view(['GET','POST'])
def usuario_api_view(request):
  if request.method=='GET':
    listausuario=User.objects.all()
    user_serializer=UserSerializer(listausuario,many=True)
    return Response(user_serializer.data, status=status.HTTP_200_OK)
  
  elif request.method=='POST':
    user_serializer=UserSerializer(data=request.data)
    if user_serializer.is_valid():
      user_serializer.save()
      return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
 
@api_view(['GET','PUT','DELETE'])
def usuario_detalle_view(request,usuario_id=None):
  usuario=User.objects.filter(id=usuario_id).first()
  if usuario:
    if request.method=='GET':
      usuario_serializer=UserSerializer(usuario)
      return Response(usuario_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
      request.data
      usuario_serializer=UserSerializer(usuario,data=request.data)
      if usuario_serializer.is_valid():
        usuario_serializer.save()
        return Response(usuario_serializer.data, status=status.HTTP_200_OK)
      return Response(usuario_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
      usuario.delete()
      return Response({'message':'Eliminado correctamente!'}, status=status.HTTP_200_OK)  
  return Response({'message':'No existe tal registro!'}, status=status.HTTP_400_BAD_REQUEST)  
