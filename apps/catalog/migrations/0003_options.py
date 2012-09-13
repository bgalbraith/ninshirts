# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'optionType'
        db.create_table('catalog_optionType', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200))
        ))
        db.send_create_signal('catalog', ['optionType'])

       
        # Adding M2M table for field categories on 'Option'
        db.create_table('catalog_option', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10), null=False),
            ('optionType', models.ForeignKey(orm['catalog.optionType'], null=False))
        ))
        db.send_create_signal('catalog', ['option'])

        # Adding M2M table for field categories on 'Product'
        db.create_table('catalog_product_options', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('option', models.ForeignKey(orm['catalog.option'], null=False))
        ))
        db.create_unique('catalog_product_options', ['product_id', 'option_id'])

    def backwards(self, orm):
        # Deleting model 'optionType'
        db.delete_table('catalog_optionType')

        # Deleting model 'option'
        db.delete_table('catalog_option')
		
        # Deleting model 'option'
        db.delete_table('catalog_product_options')
    models = {
        'catalog.optionType': {
            'Meta': {'object_name': 'optionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.option': {
            'Meta': {'object_name': 'option'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
			'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'optionType': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.optionType']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['catalog']