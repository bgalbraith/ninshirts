from django.contrib import admin
from imagekit.admin import AdminThumbnail
from apps.catalog.models import Category, Product, ProductImage, Option, \
    OptionType

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('left_id', 'right_id')
admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['admin_thumbnail']
    admin_thumbnail = AdminThumbnail(image_field='thumbnail_tiny')

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
admin.site.register(Product, ProductAdmin)
admin.site.register(Option)
admin.site.register(OptionType)