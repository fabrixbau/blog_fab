from django.db import models


from django.contrib.auth.models import User

from datetime import date


# Create your models here.
class Articulo(models.Model):

    CATEGORIA_CHOICES = (
        ("general", "General"),
        ("diseño web", "Diseño web"),
        ("programación", "Programación"),
        ("ux/ix", "UX/IX"),
    )

    titulo = models.CharField(max_length=200)
    contenido = models.TextField(default="")
    duracion = models.IntegerField(default=0)
    fecha_registro = models.DateField(default=date.today)
    categoria = models.CharField(
        max_length=50, default="general", choices=CATEGORIA_CHOICES
    )
    imagen = models.ImageField(upload_to="articulos", blank=True)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.RESTRICT)
    texto = models.TextField(default="")
    autor = models.CharField(max_length=255, default="anónimo")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.autor


class Voto(models.Model):
    comentario = models.ForeignKey(
        Comentario, on_delete=models.CASCADE, related_name="votos"
    )
    es_like = models.BooleanField(default=True)

    def __str__(self):
        estado_voto = "Me gusta" if self.es_like else "No me gusta"
        return f"{estado_voto} en {self.comentario}"
