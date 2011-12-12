from django.db import models
from itertools import chain

class Category(models.Model):
    parent = models.ForeignKey('Category', null=True)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    left_id = models.IntegerField()
    right_id = models.IntegerField()

    def __unicode__(self):
        return self.name

    def products(self):
        children = Category.objects.filter(left_id__gt=self.left_id, right_id__lt=self.right_id)
        products = [self.product_set.all()]
        for child in children:
            products.append(child.product_set.all())
        return list(chain.from_iterable(products))


class Product(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    front = models.ImageField(upload_to='products', blank=True)
    back = models.ImageField(upload_to='products', blank=True)

    def __unicode__(self):
        return self.name

    def deep_categories(self):
        categories = list(self.categories.all())
        for category in self.categories.all():
            parent = category.parent
            while parent:
                categories.append(parent)
                parent = parent.parent
        return categories