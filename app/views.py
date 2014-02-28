from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from app.serializers import CidadeSerializer, BairroSerializer, ImovelSerializer, SlideSerializer, ContatoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import Cidade, Bairro, Imovel, Adicional, Foto, Slide, Contato


class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = CidadeSerializer
    queryset = Cidade.objects.all()
    
class BairroViewSet(viewsets.ReadOnlyModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = BairroSerializer
    queryset = Bairro.objects.all()
    
class ImovelViewSet(viewsets.ReadOnlyModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = ImovelSerializer
    queryset = Imovel.objects.all()
    
class SlideViewSet(viewsets.ReadOnlyModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = SlideSerializer
    queryset = Slide.objects.all()

class ContatoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()