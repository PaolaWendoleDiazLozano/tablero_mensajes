from django.test import TestCase
from .models import Publicacion
from django.urls import reverse

# Create your tests here.
class PruebasPublicacion(TestCase):
 @classmethod
 def setUpTestData(cls):
    cls.publicacion = Publicacion.objects.create(texto='Esto es una prueba!') ##insert en base de datos

 def test_contenido_modelo(self):
   self.assertEqual(self.publicacion.texto, 'Esto es una prueba!')#desde metodo statico

def test_url_existe_ubicacion_correcta(self):
  respuesta = self.client.get('/')
  self.asserEqual(respuesta.status_code, 200)

def test_url_disponible_por_nombre(self):
  respuesta = self.client.get(reverse('inicio'))
  self.assertEqual(respuesta.status_code, 200)

def test_nombre_correcto_plantilla(self):
   respuesta = self.client.get(reverse('inicio'))
   self.assertTemplateUsed(respuesta, 'Lista_publicaciones.html')

def test_contenido_template(self):
    respuesta = self.client.get(reverse('inicio'))
    self.assertContains(respuesta, 'Esto es una prueba!')