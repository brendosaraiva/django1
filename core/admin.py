from django.contrib import admin
from .models import Produto, Cliente


# admin.ModelAdmin -> Mostra toda a ficha do produto na área administrativa
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque")


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email")


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

