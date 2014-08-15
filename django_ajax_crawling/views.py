# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from app.models import Imovel, Cidade, Bairro, Slide
from django.contrib.auth.models import User


# class LoginRequiredMixin(object):

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class IndexView(TemplateView):

    template_name = 'django_ajax_crawling/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(
            *args, **kwargs
        )
        context['imovel_list'] = Imovel.objects.where(lancamento=False)[:10]
        context['completo_list'] = Imovel.objects.where(lancamento=True)[:10]
        context['slide_list'] = Slide.objects.all()[:10]
        context['cidade_list'] = Cidade.objects.all()
        context['bairro_list'] = Bairro.objects.all()
        context['pretencoes'] = (('venda', 'Venda'),('aluguel', 'Aluguel'),('temporada', 'Temporada'),('permuta', 'Permuta'),)
        context['cidade_list'] = Cidade.objects.all()
        return context

class ImovelListView(TemplateView):
    template_name = 'django_ajax_crawling/imoveis.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ImoveisView, self).get_context_data(
            *args, **kwargs
        )
        context['imovel_list'] = Imovel.objects.filter(lancamento=False)[:40]
        return context

class CompletoListView(TemplateView):

    template_name = 'django_ajax_crawling/imoveis.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CompletosView, self).get_context_data(
            *args, **kwargs
        )
        context['imovel_list'] = Imovel.objects.filter(lancamento=True)[:40]
        return context

class ImovelView(DetailView):
    template_name = 'django_ajax_crawling/imovel.html'
    model = Imovel

index = IndexView.as_view()
imovel_list = ImovelListView.as_view()
completo_list = CompletoListView.as_view()
imovel = ImovelView.as_view()
