#from django.shortcuts import render
#from .models import Publicacion

# Create your views here.
#def lista_publicaciones(request):
   # pubs = Publicacion.objects.all()
   # return render(request, 'lista_publicaciones.html', {'publicaciones': pubs})

from django.views.generic import ListView
from .models import Publicacion

class VistaListaPublicaciones(ListView):
    model = Publicacion
    template_name = 'lista_publicaciones.html'
    context_object_name = "publicaciones"