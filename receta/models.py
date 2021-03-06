from django.db import models
from django_extensions.db.models import TimeStampedModel

DIETA = (('o', 'Omnivora'), ('v', 'Vegetariana'), ('n', "Vegana"))

# Create your models here.
class Receta(TimeStampedModel):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(blank=True, null=True, upload_to="imagenes/recetas")
    minutos_preparacion = models.SmallIntegerField()
    kcal = models.SmallIntegerField()
    dieta = models.CharField(max_length=1, choices=DIETA)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    autor = models.ForeignKey("perfil.Perfil", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Instruccion(models.Model):
    ingrediente = models.ForeignKey("Ingrediente", on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=100)
    receta = models.ForeignKey("Receta", on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.receta, self.ingrediente)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    alergeno = models.ForeignKey("Alergeno", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Alergeno(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.ImageField(blank=True, null=True, upload_to="imagenes/alergenos")

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(blank=True, null=True, upload_to="imagenes/categorias")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

