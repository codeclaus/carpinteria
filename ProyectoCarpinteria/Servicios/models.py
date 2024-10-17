from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    image = models.ImageField(
        upload_to='categorias', null=True, blank=True)
    name = models.CharField(max_length=40)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class ProductosLavadora(models.Model):
    image = models.ImageField(
        upload_to='categorias/lavadoras', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name = "lavadora"
        verbose_name_plural = "lavadoras"
        ordering = ['modelo']

    def __str__(self) -> str:
        return self.modelo + " " + self.marca
