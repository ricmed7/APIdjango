from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken 
from .serializer import UserSerializer

class Login(ObtainAuthToken):
    def post(self, request,*args,**kwards):
        #print(request.user)
        login_serializer=self.serializer_class(data=request.data,context={'request':request})
        if login_serializer.is_valid():
            #print("paso validacion")
            user=login_serializer.validated_data['user']
            if user.is_active:
                token,created=Token.objects.get_or_create(user=user)
                user_serializer=UserSerializer(user)
                if created:
                    return Response({
                                     'token':token.key,
                                     'user':user_serializer.data,
                                     'message':'inicio de sesion correcto'
                                    },status=status.HTTP_201_CREATED)  
                else:
                    #eliminando sesiones abiertas, cuando se intenta ingresar al mismo tiempo
                    todas_sesiones=Session.objects.filter(expire_date__gte=datetime.now())
                    if todas_sesiones.exists():
                        for sesion in todas_sesiones:
                            datos_sesion=sesion.get_decoded()
                            if user.id == int(datos_sesion.get('_auth_user_id')):
                              sesion.delete()
                    token.delete()
                    token=Token.objects.create(user=user)
                    return Response({
                                     'token':token.key,
                                     'user':user_serializer.data,
                                     'message':'inicio de sesion correcto1'
                                    },status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesion'},status=status.HTTP_401_UNAUTHORIZED)  
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos'},status=status.HTTP_400_BAD_REQUEST)        
        #return Response({'mensaje':'hola necesitamos un token'},status=status.HTTP_200_OK)
class Logaut(APIView):
    def get(self,request,*args,**kwards):
      try:
        token=request.GET.get('token')
        token=Token.objects.filter(key=token).first()
        if token:
          user=token.user
            
          todas_sesiones=Session.objects.filter(expire_date__gte=datetime.now())
          if todas_sesiones.exists():
            for sesion in todas_sesiones:
              datos_sesion=sesion.get_decoded()
              if user.id == int(datos_sesion.get('_auth_user_id')):
                sesion.delete()   
          token.delete()
          return Response({'token_message':'token eliminado','session_message':'Sesiones eliminadas'},status=status.HTTP_200_OK)
        return Response({'error':'Usuario no encontrado'},status=status.HTTP_400_BAD_REQUEST)
      except:
         return Response({'error':'No se encontro token'},status=status.HTTP_409_CONFLICT)




            
