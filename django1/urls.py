"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404, handler500  # Gerencia a página de errors

from core import views

# include -> Função que pega o caminho de uma aplicação e atribui a rota.

# path("", include("core.urls")) -> Toda requisição feita para
# raiz é enviada (include) para aplicação core, que tem o arquivo
# urls que irá receber essas requisições.

urlpatterns = [
    path("acesso/", admin.site.urls),
    path("", include("core.urls")),
]

handler404 = views.error404
handler500 = views.error500



