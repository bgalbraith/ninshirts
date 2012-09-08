# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('catalog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Category'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('left_id', self.gf('django.db.models.fields.IntegerField')()),
            ('right_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('catalog', ['Category'])

        # Adding model 'Product'
        db.create_table('catalog_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('front', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('back', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('catalog', ['Product'])

        # Adding M2M table for field categories on 'Product'
        db.create_table('catalog_product_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['catalog.product'], null=False)),
            ('category', models.ForeignKey(orm['catalog.category'], null=False))
        ))
        db.create_unique('catalog_product_categories', ['product_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('catalog_category')

        # Deleting model 'Product'
        db.delete_table('catalog_product')

        # Removing M2M table for field categories on 'Product'
        db.delete_table('catalog_product_categories')


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
        'catalog.product': {
            'Meta': {'object_name': 'Product'},
            'back': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.Category']", 'symmetrical': 'False'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'front': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']