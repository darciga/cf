from django.contrib import admin
from blog.models import Comentario, Entrada, Estado, Categoria


admin.site.register(Comentario)
admin.site.register(Entrada)
admin.site.register(Estado)
admin.site.register(Categoria)