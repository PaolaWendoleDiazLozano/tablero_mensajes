from django.urls import path
from .views import VistaListaPublicaciones

urlpatterns = [
    path('', VistaListaPublicaciones.as_view(), name='inicio'),
]