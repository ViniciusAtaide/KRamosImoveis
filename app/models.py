#-*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import signals


# Slug
def slug_pre_save(signal, instance, sender, **kwargs):
    if hasattr(instance, 'slug_conf') and not getattr(instance, instance.slug_conf['field'], None):
        slug = slugify(getattr(instance, instance.slug_conf['from'], None))
        new_slug = slug
        counter = 0
        while sender.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            counter += 1
            new_slug = '%s-%d' % (slug, counter)
        setattr(instance, instance.slug_conf['field'], new_slug)


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.nome)


class Bairro(models.Model):
    cidade = models.ForeignKey(to=Cidade, related_name="bairros")
    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ('cidade', 'nome')

    def __unicode__(self):
        return u'%s - %s' % (self.nome, self.cidade)

class Adicional(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.nome)

PRETENSAO_VALORES = (
    ('venda', 'Venda'),
    ('aluguel', 'Aluguel'),
    ('temporada', 'Temporada'),
    ('permuta', 'Permuta'),
)

POSICAO_VALORES = (
    ('Norte', 'Norte'),
    ('Sul', 'Sul'),
    ('Nascente', 'Nascente'),
    ('Poente', 'Poente'),
    ('Nascente Norte', 'Nascente Norte'),
    ('Nascente Sul', 'Nascente Sul'),
    ('Poente Norte', 'Poente Norte'),
    ('Poente Sul', 'Poente Sul'),
)


class Imovel(models.Model):

    class Meta:
        verbose_name = u'Imóvel'
        verbose_name_plural = u'Imóveis'

    bairro      = models.ForeignKey(Bairro)
    slug        = models.SlugField(blank=True, help_text=u'deixe este campo em branco')
    nome        = models.CharField(max_length=200)
    pretencao   = models.CharField(u'Pretensão', max_length=50, choices=PRETENSAO_VALORES)
    descricao   = models.TextField(u'Descrição')
    chamada     = models.TextField()
    imagem      = models.ImageField(upload_to='imovel', blank=True)
    quartos     = models.IntegerField()
    suites      = models.IntegerField()
    banheiros   = models.IntegerField()
    salas       = models.IntegerField()
    cozinhas    = models.IntegerField()
    varandas    = models.IntegerField()
    vagas       = models.IntegerField()
    terreno     = models.CharField(max_length=50, help_text='campo texto, colocar m² ou 1 x 1 m')
    posicao     = models.CharField(u'Posição', max_length=50, choices=POSICAO_VALORES)
    construida  = models.CharField(u'Área Construida', max_length=50, help_text='campo texto, colocar m² ou 1 x 1 m')
    adicionais  = models.ManyToManyField(Adicional)
    valor       = models.CharField(max_length=200, help_text='Valor pode ser um texto, não esqueça do nome da moeda (R$)')
    valor_num   = models.DecimalField(max_digits=20, decimal_places=2, help_text='Valor para busca')
    lancamento  = models.BooleanField(u'Lançamento', default=False)
    entrega     = models.DateTimeField('Data de Entrega', null = True, blank=True)
    publicar    = models.BooleanField(default=True)

    slug_conf = {'field': 'slug', 'from': 'nome'}

    def __unicode__(self):
        return u'{0}'.format(self.nome)

signals.pre_save.connect(slug_pre_save, sender=Imovel)

class Slide(models.Model):
    imagem  = models.ImageField(upload_to='slide')
    ordem   = models.IntegerField()
    texto1  = models.CharField(max_length=30)
    texto2  = models.CharField(max_length=50)
    url     = models.URLField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.imagem)

class Foto(models.Model):
    imagem  = models.ImageField(upload_to='foto')
    ordem   = models.IntegerField(blank=True)
    imovel  = models.ForeignKey(Imovel, related_name='fotos')

    def __unicode__(self):
        return u'{0}'.format(self.foto)

class Contato(models.Model):
    nome        = models.CharField(max_length=200)
    telefone    = models.CharField(max_length=50)
    email       = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{0}'.format(self.nome)
