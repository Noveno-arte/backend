from rest_framework import serializers
from recetas.models import Receta

class RecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['id', 'titulo', 'imagen']

class RecetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receta
        fields = ['id', 'titulo', 'imagen', 'ingredientes', 'preparacion']