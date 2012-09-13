from django.contrib import admin
from apps.catalog.models import Category, Product, Option, OptionType

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('left_id', 'right_id')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Option)
admin.site.register(OptionType)