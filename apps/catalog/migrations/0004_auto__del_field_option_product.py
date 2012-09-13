# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field options on 'Product'
        db.create_table('catalog_product_options', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('option', models.ForeignKey(orm['catalog.option'], null=False))
        ))
        db.create_unique('catalog_product_options', ['product_id', 'option_id'])

        # Deleting field 'Option.product'
        db.delete_column('catalog_option', 'product_id')


    def backwards(self, orm):
        # Removing M2M table for field options on 'Product'
        db.delete_table('catalog_product_options')

        # Adding field 'Option.product'
        db.add_column('catalog_option', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['catalog.Product']),
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
            'back': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'front': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Option']", 'symmetrical': 'False'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']