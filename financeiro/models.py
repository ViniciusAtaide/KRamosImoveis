# coding: utf-8
from django.db import models


# Create your models here.

class Imovel(models.Model):
	nome 	= models.CharField(max_length=250)
	ativo 	= models.BooleanField(default=False)

class Alguel(models.Model):
	imovel 		= models.ForeignKey(Imovel)
	inquilino 	= models.CharField(max_length=250)
	vencimento 	= models.IntegerField()
	aluguel 	= models.DecimalField(max_digits=20,decimal_places=2)
	condominio 	= models.DecimalField(max_digits=20,decimal_places=2)
	taxa 		= models.DecimalField(max_digits=20,decimal_places=2)
	reajuste 	= models.DateField()
	contrato 	= models.DateField()

class Temporada(models.Model):
	imovel 		= models.ForeignKey(Imovel)
	inicio		= models.DateField()
	fim			= models.DateField()
	locatario   = models.CharField(max_length=250)
	total		= models.DecimalField(max_digits=20,decimal_places=2)
	reserva     = models.DecimalField(max_digits=20,decimal_places=2)
	data_res    = models.DateField()
	assinatura	= models.DecimalField(max_digits=20,decimal_places=2)
	data_ass	= models.DateField()
	caucao		= models.DecimalField(max_digits=20,decimal_places=2)
	taxa_res	= models.DecimalField(max_digits=20,decimal_places=2)
	taxa_ass	= models.DecimalField(max_digits=20,decimal_places=2)


TIPO_VALORES = (
    ('entrada', 'Entrada'),
    ('saida', u'Saída'),
    ('deposito', u'Depósito'),
)

class Conta(models.Model):
	imovel 		= models.ForeignKey(Imovel)
	data 		= models.DateField()
	discriminacao	= models.CharField(max_length=250)
	tipo		= models.CharField(max_length=50, choices=TIPO_VALORES)

class Venda(models.Model):
	imovel 	= models.CharField(max_length=250)
	data 	= models.DateField()
	valor 	= models.DecimalField(max_digits=20,decimal_places=2)
	taxa 	= models.DecimalField(max_digits=20,decimal_places=2)

