# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imovel'
        db.create_table(u'financeiro_imovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'financeiro', ['Imovel'])

        # Adding model 'Alguel'
        db.create_table(u'financeiro_alguel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.Imovel'])),
            ('inquilino', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('vencimento', self.gf('django.db.models.fields.IntegerField')()),
            ('aluguel', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('condominio', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('taxa', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('reajuste', self.gf('django.db.models.fields.DateField')()),
            ('contrato', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'financeiro', ['Alguel'])

        # Adding model 'Temporada'
        db.create_table(u'financeiro_temporada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.Imovel'])),
            ('inicio', self.gf('django.db.models.fields.DateField')()),
            ('fim', self.gf('django.db.models.fields.DateField')()),
            ('locatario', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('reserva', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('data_res', self.gf('django.db.models.fields.DateField')()),
            ('assinatura', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('data_ass', self.gf('django.db.models.fields.DateField')()),
            ('caucao', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('taxa_res', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('taxa_ass', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'financeiro', ['Temporada'])

        # Adding model 'Conta'
        db.create_table(u'financeiro_conta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.Imovel'])),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('discriminacao', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'financeiro', ['Conta'])

        # Adding model 'Venda'
        db.create_table(u'financeiro_venda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('taxa', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'financeiro', ['Venda'])


    def backwards(self, orm):
        # Deleting model 'Imovel'
        db.delete_table(u'financeiro_imovel')

        # Deleting model 'Alguel'
        db.delete_table(u'financeiro_alguel')

        # Deleting model 'Temporada'
        db.delete_table(u'financeiro_temporada')

        # Deleting model 'Conta'
        db.delete_table(u'financeiro_conta')

        # Deleting model 'Venda'
        db.delete_table(u'financeiro_venda')


    models = {
        u'financeiro.alguel': {
            'Meta': {'object_name': 'Alguel'},
            'aluguel': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'condominio': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'contrato': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['financeiro.Imovel']"}),
            'inquilino': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'reajuste': ('django.db.models.fields.DateField', [], {}),
            'taxa': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'vencimento': ('django.db.models.fields.IntegerField', [], {})
        },
        u'financeiro.conta': {
            'Meta': {'object_name': 'Conta'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'discriminacao': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['financeiro.Imovel']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'financeiro.imovel': {
            'Meta': {'object_name': 'Imovel'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'financeiro.temporada': {
            'Meta': {'object_name': 'Temporada'},
            'assinatura': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'caucao': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'data_ass': ('django.db.models.fields.DateField', [], {}),
            'data_res': ('django.db.models.fields.DateField', [], {}),
            'fim': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['financeiro.Imovel']"}),
            'inicio': ('django.db.models.fields.DateField', [], {}),
            'locatario': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'reserva': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'taxa_ass': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'taxa_res': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        u'financeiro.venda': {
            'Meta': {'object_name': 'Venda'},
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'taxa': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        }
    }

    complete_apps = ['financeiro']