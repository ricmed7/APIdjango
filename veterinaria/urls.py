from django.urls import path,include
from rest_framework import routers
from .api_propietario import propietario_api_view,propietario_detalle_view
from .api_especie import especie_api_view,especie_detalle_view
from .api_mascota import mascota_api_view,mascota_detalle_view
from .api_consulta import consulta_api_view,consulta_detalle_view
from .api_usuario import usuario_api_view,usuario_detalle_view
#from .token_login import Login

'''router=routers.DefaultRouter()
router.register(r'propietario',views.PropietarioViewset)
router.register(r'especie',views.EspecieViewset)

urlpatterns=[
    path('',include(router.urls))
]'''
urlpatterns=[
    #path('',Login.as_view,name='login'),
    path('propietario/',propietario_api_view,name='listapropietario.show'),
    path('propietario/<int:propietario_id>',propietario_detalle_view,name='datopropietario.show'),
    path('especie/',especie_api_view,name='listaespecie.show'),
    path('especie/<int:especie_id>',especie_detalle_view,name='datoespecie.show'),
    path('mascota/',mascota_api_view,name='listamascota.show'),
    path('mascota/<int:mascota_id>',mascota_detalle_view,name='datomascota.show'),
    path('consulta/',consulta_api_view,name='consulta.show'),
    path('consulta/<int:consulta_id>',consulta_detalle_view,name='datoconsulta.show'),
    path('usuario/',usuario_api_view,name='usuario.show'),
    path('usuario/<int:usuario_id>',usuario_detalle_view,name='datousuario.show')
]
