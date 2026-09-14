#from django.shortcuts import render
#from .models import Publicacion

# Create your views here.
#def lista_publicaciones(request):
   # pubs = Publicacion.objects.all()
   # return render(request, 'lista_publicaciones.html', {'publicaciones': pubs})

from django.views.generic import ListView
from .models import Publicacion

class ListaPublicaciones(ListView):
    model = Publicacion
    template_name = 'Lista_publicaciones.html'