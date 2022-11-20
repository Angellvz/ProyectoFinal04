from rest_framework import serializers
from .models import Usuario,Comentarios,Empresas,Arduino,Vehiculos,Rutas

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'name', 'correo', 'password', 'tipo')
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('id', 'comentario', 'release_date', 'usuario')
class EmpresasSerializer(serializers.ModelSerializer):
     class Meta:
        model = Empresas
        fields = ('id', 'nombre')
class ArduinoSerializer(serializers.ModelSerializer):
     class Meta:
        model = Arduino
        fields = ('id', 'coordenadas')
class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = ('id', 'placa', 'arduino', 'empresa')
class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = ('id', 'ruta', 'empresa', 'arduino', 'vehiculo')           