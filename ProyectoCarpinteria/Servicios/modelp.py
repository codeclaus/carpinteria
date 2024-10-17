from django.db import models
from django.contrib.auth.models import User
from .models import Categoria


class Temas(models.Model):
    class TemasL(models.TextChoices):
        OPCION_1 = 'PYTHON', 'PYTHON'
        OPCION_2 = 'UI', 'UI'
        OPCION_3 = 'JAVASCRIPT', 'JAVASCRIPT'
        OPCION_4 = 'VARIOS', 'VARIOS'

    class Meta:
        verbose_name = "tema"
        verbose_name_plural = "temas"
        ordering = ['name']

    def __str__(self) -> str:
        return str(self.name)

    name = models.CharField(
        choices=TemasL.choices, default=TemasL.OPCION_1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ProgrammingTopics(models.Model):
    class Desarrollo(models.IntegerChoices):
        PENDIENTE = 1, 'Pendiente'
        EN_PROCESO = 2, 'En Proceso'
        COMPLETADO = 3, 'Completado'
    image = models.ImageField(
        upload_to="categorias/programming", null=True, blank=True)
    titulo = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    tema = models.ManyToManyField(Temas)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    desarrollo = models.IntegerField(
        choices=Desarrollo.choices, default=Desarrollo.PENDIENTE)
    comentario = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Programacion"
        verbose_name_plural = "Programaciones"
        ordering = ['titulo']

    def __str__(self) -> str:
        return self.titulo
