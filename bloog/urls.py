from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contenido/<int:articulo_id>", views.contenido, name="contenido"),
    path("comentar/<int:articulo_id>", views.comentar, name="comentar"),
    path("votar/<int:comentario_id>/<str:es_like>/", views.voto, name="voto"),
]
