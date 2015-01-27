from django.contrib.admin import AdminSite
from .models import Imovel, Alguel, Temporada, Conta, Venda

# Registro do novo admin para a urlsconf
class FinanceiroAdminSite(AdminSite):
    site_header = 'Financeiro'

admin_site = FinanceiroAdminSite(name='financeiro')
#########


# Modelos padroes
admin_site.register(Imovel)
admin_site.register(Alguel)
admin_site.register(Temporada)
admin_site.register(Conta)
admin_site.register(Venda)
# Exemplo de um modelo com override
# admin_site.register(Imovel, ImovelAdmin)
