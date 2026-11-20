from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("texto", "autor", "fecha")
    list_filter = ("fecha", "autor")