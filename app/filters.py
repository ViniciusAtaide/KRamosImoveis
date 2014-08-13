import django_filters
from models import Imovel

class ImovelFilter(django_filters.FilterSet):
	pretencao = django_filters.CharFilter(name="pretencao", lookup_type="contains")
	lancamento = django_filters.CharFilter(name="lancamento", lookup_type="contains")
	
	class Meta:
		model = Imovel
		fields = ['pretencao','lancamento']