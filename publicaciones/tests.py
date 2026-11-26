from django.test import TestCase
from django.urls import reverse
from .models import Publicacion


class PruebasPublicacion(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.publicacion = Publicacion.objects.create(texto='Esto es una prueba!')

    def test_contenido_modelo(self):
        self.assertEqual(self.publicacion.texto, 'Esto es una prueba!')

    def test_url_existe_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correcto_plantilla(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(respuesta, 'lista_publicaciones.html')

    def test_contenido_template(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertContains(respuesta, 'Esto es una prueba!')


class TableroVacioTests(TestCase):
    def test_base_de_datos_vacia_muestra_mensaje(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Todavía no hay mensajes.')