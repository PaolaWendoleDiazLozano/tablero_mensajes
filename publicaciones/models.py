from django.db import models

class Publicacion(models.Model):
    texto = models.TextField()
    autor = models.CharField(max_length=100, default="Anónimo")
    fecha = models.DateTimeField("fecha de publicación", auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.autor}: {self.texto[:50]}"