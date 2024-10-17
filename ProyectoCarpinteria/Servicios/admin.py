from django.contrib import admin
from .models import Categoria, ProductosLavadora
from .modelp import Temas, ProgrammingTopics
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(ProductosLavadora)
admin.site.register(Temas)
admin.site.register(ProgrammingTopics)
