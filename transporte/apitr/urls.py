from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    #Usuario
    path('usuario',views.UsuarioView.as_view(),name='usuario'),
    path('usuario/<int:serie_id>',views.UsuarioDetailView.as_view()),
    #Comentarios
    path('comentarios',views.ComentariosView.as_view(),name='comentarios'),
    path('comentarios/<int:serie_id>',views.ComentariosDetailView.as_view()),
    #Empresas
    path('empresas',views.EmpresasView.as_view(),name='empresas'),
    path('empresas/<int:serie_id>',views.EmpresasDetailView.as_view()),
    #Arduino
    path('arduino',views.ArduinoView.as_view(),name='arduino'),
    path('arduino/<int:serie_id>',views.ArduinoDetailView.as_view()),
    #Vehiculos
    path('vehiculos',views.VehiculosView.as_view(),name='vehiculos'),
    path('vehiculos/<int:serie_id>',views.VehiculosDetailView.as_view()),
    #Rutas
    path('rutas',views.RutasView.as_view(),name='rutas'),
    path('rutas/<int:serie_id>',views.RutasDetailView.as_view())
]
