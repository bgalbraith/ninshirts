from django.contrib import admin
from apps.catalog.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)