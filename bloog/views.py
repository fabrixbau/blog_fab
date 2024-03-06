from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Articulo, Comentario, Voto
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logea al usuario inmediatamente después de registrarse
            return redirect('index')  # Redirecciona al inicio o a la página que desees
    else:
        form = UserCreationForm()
    return render(request, 'bloog/register.html', {'form': form})