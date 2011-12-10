from django.db import models
from itertools import chain

class Category(models.Model):
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
    front = models.ImageField(upload_to='shirts', blank=True)
    back = models.ImageField(upload_to='shirts', blank=True)

    def __unicode__(self):
        return self.name