from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Usuario,Comentarios,Empresas,Arduino,Vehiculos,Rutas
from .serializers import UsuarioSerializer,ComentariosSerializer,EmpresasSerializer,ArduinoSerializer,VehiculosSerializer,RutasSerializer
#Index View
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
#View Usuarios    
class UsuarioView(APIView):
    
    def get(self,request):
        dataSeries = Usuario.objects.all()
        serSeries = UsuarioSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = UsuarioSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class UsuarioDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Usuario.objects.get(pk=serie_id)
        serSerie = UsuarioSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Usuario.objects.get(pk=serie_id)
        serSerie = UsuarioSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Usuario.objects.get(pk=serie_id)
        serSerie = UsuarioSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
#View Comentarios
class ComentariosView(APIView):
    
    def get(self,request):
        dataSeries = Comentarios.objects.all()
        serSeries = ComentariosSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = ComentariosSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class ComentariosDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Comentarios.objects.get(pk=serie_id)
        serSerie = ComentariosSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Comentarios.objects.get(pk=serie_id)
        serSerie = ComentariosSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Comentarios.objects.get(pk=serie_id)
        serSerie = ComentariosSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
#View Empresas 
class EmpresasView(APIView):
    
    def get(self,request):
        dataSeries = Empresas.objects.all()
        serSeries = EmpresasSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = EmpresasSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class EmpresasDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Empresas.objects.get(pk=serie_id)
        serSerie = EmpresasSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Empresas.objects.get(pk=serie_id)
        serSerie = EmpresasSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Empresas.objects.get(pk=serie_id)
        serSerie = EmpresasSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
#View Arduino
class ArduinoView(APIView):
    
    def get(self,request):
        dataSeries = Arduino.objects.all()
        serSeries = ArduinoSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = ArduinoSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class ArduinoDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Arduino.objects.get(pk=serie_id)
        serSerie = ArduinoSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Arduino.objects.get(pk=serie_id)
        serSerie = ArduinoSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Arduino.objects.get(pk=serie_id)
        serSerie = ArduinoSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
#View Vehiculos
class VehiculosView(APIView):
    
    def get(self,request):
        dataSeries = Vehiculos.objects.all()
        serSeries = VehiculosSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = VehiculosSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class VehiculosDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Vehiculos.objects.get(pk=serie_id)
        serSerie = VehiculosSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Vehiculos.objects.get(pk=serie_id)
        serSerie = VehiculosSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Vehiculos.objects.get(pk=serie_id)
        serSerie = VehiculosSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
#View Rutas
class RutasView(APIView):
    
    def get(self,request):
        dataSeries = Rutas.objects.all()
        serSeries = RutasSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = RutasSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class RutasDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Rutas.objects.get(pk=serie_id)
        serSerie = RutasSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Rutas.objects.get(pk=serie_id)
        serSerie = RutasSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Rutas.objects.get(pk=serie_id)
        serSerie = RutasSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)


