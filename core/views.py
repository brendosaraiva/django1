from django.shortcuts import render
from django.shortcuts import get_object_or_404  # Apresenta erro de página não encontrada

from django.http import HttpResponse  # Formato de páginas de erros
from django.template import loader

from .models import Produto

# view -> no django, nada mais é do que uma função,
# função que recebe uma variável (request) de requisição para
# acessar determinada página web.

# render -> renderiza uma página/template html, ou seja, carrega.

# Criando primeira view django

# Qualquer variável que for acrescentada na view index (página raiz)
# poderá ser acessada na sua página alvo (HTML) ao ser renderizada em render.


def index(request):
    produtos = Produto.objects.all()

    context = {
        "curso": "Programação Web com Django Framework",
        "outro": "Django é massa!",
        "produtos": produtos
    }
    return render(request, "index.html", context)


# Criando segunda view django
def contato(request):
    return render(request, "contato.html")


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)  # get(id=pk) -> filtra dados por id
    prod = get_object_or_404(Produto, id=pk)
    context = {
        "produto": prod
    }
    return render(request, "produto.html", context)


def error404(request, ex):
    template = loader.get_template("404.html")
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)


def error500(request):
    template = loader.get_template("500.html")
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)
