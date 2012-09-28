from django.contrib import admin
from django.db.models import Max
from imagekit.admin import AdminThumbnail
from apps.catalog.models import Category, Product, ProductImage, Option, \
    OptionType

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('left_id', 'right_id')

    list_display = ['ascii_branch']
    def ascii_branch(self, obj):
        depth = obj.depth()
        return ('--' * (depth - 1)) + ' ' + obj.name
    ascii_branch.short_description = 'Category'


    def save_model(self, request, obj, form, change):
        reorganize = True
        if change:
            ref = Category.objects.get(pk=obj.id)
            if ref.parent == obj.parent:
                reorganize = False
        if reorganize:
            anchor = obj.parent
            if anchor is None:
                insert = Category.objects.aggregate(
                    Max('right_id'))['right_id__max']
            else:
                insert = obj.parent.right_id
            for c in Category.objects.filter(left_id__gt=insert):
                c.left_id += 2
                c.save()
            for c in Category.objects.filter(right_id__gte=insert):
                c.right_id += 2
                c.save()
            obj.left_id = insert
            obj.right_id = insert + 1

        obj.save()

    def delete_model(self, request, obj):
        for c in Category.objects.filter(left_id__gt=obj.right_id):
            c.left_id -= 2
            c.save()
        for c in Category.objects.filter(right_id__gte=obj.right_id):
            c.right_id -= 2
            c.save()

        obj.product_set.clear()
        obj.delete()

admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['admin_thumbnail']
    admin_thumbnail = AdminThumbnail(image_field='thumbnail_tiny')

class ProductAdmin(admin.ModelAdmin):
    ordering = ['name']
    inlines = [
        ProductImageInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Option)
admin.site.register(OptionType)