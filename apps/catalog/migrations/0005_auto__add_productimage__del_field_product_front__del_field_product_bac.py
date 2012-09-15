# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductImage'
        db.create_table('catalog_productimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
            ('original', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('catalog', ['ProductImage'])

        # Deleting field 'Product.front'
        db.delete_column('catalog_product', 'front')

        # Deleting field 'Product.back'
        db.delete_column('catalog_product', 'back')


    def backwards(self, orm):
        # Deleting model 'ProductImage'
        db.delete_table('catalog_productimage')

        # Adding field 'Product.front'
        db.add_column('catalog_product', 'front',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Product.back'
        db.add_column('catalog_product', 'back',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True),
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
            'option_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.OptionType']"})
        },
        'catalog.optiontype': {
            'Meta': {'object_name': 'OptionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Option']", 'symmetrical': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.productimage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'ProductImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.Product']"})
        }
    }

    complete_apps = ['catalog']