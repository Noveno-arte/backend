from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=80)
    imagen = models.CharField(max_length=120, default="https://i.blogs.es/87930e/comidas-ricas/1366_2000.jpg")
    creado = models.DateTimeField(auto_now_add=True)
    ingredientes = models.JSONField()
    preparacion = models.JSONField()

    class Meta:
        ordering = ['creado']

"""
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.PositiveSmallIntegerField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return '%s' % (self.nombre)

class Preparacion(models.Model):
    paso = models.TextField(max_length=500)
    numero = models.PositiveSmallIntegerField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return '%s' % (self.paso)
"""