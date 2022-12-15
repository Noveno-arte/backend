from recetas.models import Receta
from recetas.serializers import RecetasSerializer, RecetaSerializer
from rest_framework import generics
from django.http import HttpResponse
import os

class RecetaNueva(generics.CreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    def post(self,request,*args,**kwargs):
        titulo = request.data['titulo']
        imagen = request.data['imagen']
        ingredientes = request.data['ingredientes'].split('<<separation>>')
        preparacion = request.data['preparacion'].split('<<separation>>')
        Receta.objects.create(titulo=titulo,imagen=imagen,ingredientes=ingredientes,preparacion=preparacion)
        return HttpResponse({'message':'receta creada'},status=200)


class RecetaList(generics.ListAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetasSerializer 
    
#Para probar la creacion de recetas directamente en el server de Django.
# En caso de ser así, descomentar las siguientes lineas y comentar la class RecetaList(...) anterior
"""
class RecetaList(generics.ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer #para testing
"""

class RecetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    def put(self,request,*args,**kwargs):
        _id = request.data['id']
        titulo = request.data['titulo']
        imagen = request.data['imagen']
        ingredientes = request.data['ingredientes'].split('<<separation>>')
        preparacion = request.data['preparacion'].split('<<separation>>')

        receta = Receta.objects.get(id=_id)
        
        if len(request.FILES) !=0:
            try:
                os.remove(receta.imagen.path)
            except:
                pass
            finally:
                receta.imagen = request.FILES['imagen']
        
        receta.titulo = titulo
        receta.ingredientes = ingredientes
        receta.preparacion = preparacion

        receta.save()

        return HttpResponse({'message':'receta actualizada'},status=200)