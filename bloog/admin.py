from django.contrib import admin

# Register your models here.
from .models import Articulo


# admin.site.register(Articulo)
@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):

    list_display = ("titulo", "imagen", "autor")
