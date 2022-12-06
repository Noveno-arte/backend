from recetas.models import Receta
from recetas.serializers import RecetasSerializer, RecetaSerializer
from rest_framework import generics

class RecetaNueva(generics.CreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

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