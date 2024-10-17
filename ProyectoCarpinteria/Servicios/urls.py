from django.urls import path
from .views import Categorias, ProductosLavadoraView, ProgrammingTopicsView

urlpatterns = [
    path('', Categorias, name="categorias"),
    path('lavadoras/<int:pk>/',
         ProductosLavadoraView, name="lavadoras"),
    path('programming/<int:pk>/',
         ProgrammingTopicsView, name="programming"),

]
