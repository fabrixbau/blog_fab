from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Articulo, Comentario, Voto
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    listaArticulos = Articulo.objects.all()

    # Añadir impresión para depuración
    for articulo in listaArticulos:
        print(articulo.titulo, articulo.autor.first_name, articulo.autor.last_name)

    context = {"articulos": listaArticulos}

    return render(request, "bloog/index.html", context)


def contenido(request, articulo_id):

    objArticulo = Articulo.objects.get(pk=articulo_id)
    listaComentarios = Comentario.objects.filter(articulo=objArticulo)

    context = {"articulo": objArticulo, "comentarios": listaComentarios}

    return render(request, "bloog/articulo.html", context)


def comentar(request, articulo_id):

    objArticulo = Articulo.objects.get(pk=articulo_id)

    if request.method == "POST":
        comentario = request.POST["comentario"]
        print(comentario)
        nuevoComentario = Comentario()
        nuevoComentario.texto = comentario
        nuevoComentario.articulo = objArticulo
        nuevoComentario.save()

        return redirect("/contenido/" + str(articulo_id))


@csrf_exempt
def voto(request, comentario_id, es_like):
    if request.method == "POST":
        comentario = get_object_or_404(Comentario, pk=comentario_id)
        if es_like == "like":
            comentario.likes += 1
        elif es_like == "dislike":
            comentario.dislikes += 1
        comentario.save()

        return JsonResponse(
            {"likes": comentario.likes, "dislikes": comentario.dislikes}
        )
