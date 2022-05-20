from django.contrib import admin
from .models import autor, obras, categorias
# Register your models here.

admin.site.register(autor)
admin.site.register(obras)
admin.site.register(categorias)
