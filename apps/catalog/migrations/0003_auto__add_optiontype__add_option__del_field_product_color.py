# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OptionType'
        db.create_table('catalog_optiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('catalog', ['OptionType'])

        # Adding model 'Option'
        db.create_table('catalog_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
            ('option_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.OptionType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('catalog', ['Option'])

        # Deleting field 'Product.color'
        db.delete_column('catalog_product', 'color')


    def backwards(self, orm):
        # Deleting model 'OptionType'
        db.delete_table('catalog_optiontype')

        # Deleting model 'Option'
        db.delete_table('catalog_option')

        # Adding field 'Product.color'
        db.add_column('catalog_product', 'color',
                      self.gf('django.db.models.fields.CharField')(default='n/a', max_length=20),
                      keep_default=False)


    models = {
        'catalog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left_id': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Category']", 'null': 'True'}),
            'right_id': ('django.db.models.fields.IntegerField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.option': {
            'Meta': {'object_name': 'Option'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'option_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.OptionType']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        },
        'catalog.optiontype': {
            'Meta': {'object_name': 'OptionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'back': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'front': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']