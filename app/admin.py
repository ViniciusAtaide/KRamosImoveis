#-*- coding: utf-8 -*-
from django.contrib import admin
from app.models import Cidade, Bairro, Imovel, Adicional, Slide, Foto, Contato

class BairroInline(admin.TabularInline):
	model = Bairro
	extra = 3

class CidadeAdmin(admin.ModelAdmin):
	fieldsets = [
		(u'Descrição', {'fields':['nome']}),
	]
	inlines = [BairroInline]

class BairroAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cidade')
	list_filter = ['cidade']

class FotoInLine(admin.TabularInline):
	model = Foto
	extra = 5

class ImovelAdmin(admin.ModelAdmin):
	fieldsets = [
		(u'Descrição', {'fields':['pretencao','nome','descricao','chamada','imagem', 'valor', 'valor_num']}),
		(u'Localização', {'fields': ['bairro']}),
		('Atributos', {'fields':['quartos', 'suites', 'banheiros', 'salas', 'cozinhas', 'varandas', 'vagas', 
			'terreno', 'construida', 'posicao']}),
		('Adicionais', {'fields': ['adicionais']}),
		(u'Outras características', {'fields': ['lancamento', 'entrega', 'publicar']}),
		('Slug', {'fields': ['slug'], 'classes': ['collapse']}),
	]

	inlines = [FotoInLine]
	list_display = ('nome', 'bairro', 'pretencao', 'quartos', 'valor', 'publicar')
	list_filter = ['pretencao', 'quartos', 'publicar', 'lancamento', 'bairro']
	search_fields = ['nome']

class SlideAdmin(admin.ModelAdmin):
	list_display = ('imagem','texto1', 'texto2', 'ordem', 'url')

class FotoAdmin(admin.ModelAdmin):
	list_display = ('imagem','imovel','ordem')
	list_filter = ['imovel']

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'email')
	search_fields = ['nome']

admin.site.register(Slide, SlideAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Imovel,ImovelAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Bairro, BairroAdmin)
admin.site.register(Adicional)
admin.site.register(Contato, ContatoAdmin)
