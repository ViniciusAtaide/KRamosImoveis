from django.forms import widgets
from rest_framework import serializers
from app.models import Cidade, Bairro, Imovel, Adicional, Foto, Slide, Contato

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id', 'nome')

class BairroSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer(many=False, read_only=True)

    class Meta:
        model = Bairro
        fields = ('id', 'nome', 'cidade')

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ('imagem', 'ordem')

class ImovelSerializer(serializers.ModelSerializer):
    bairro = BairroSerializer(many=False, read_only=True)
    adicionais = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nome')
    fotos = FotoSerializer(many=True, read_only=True)

    class Meta:
        model = Imovel
        fields = ('id', 'bairro', 'slug', 'nome', 'pretencao', 'descricao', 'chamada', 'imagem', 'quartos',
                  'terreno', 'construida', 'posicao', 'suites', 'banheiros', 'salas', 'cozinhas', 'varandas',
                   'vagas', 'adicionais', 'valor', 'valor_num', 'lancamento', 'entrega', 'publicar', 'fotos')

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('id', 'imagem', 'texto1', 'texto2', 'ordem', 'url')

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('id', 'nome', 'telefone', 'email')
