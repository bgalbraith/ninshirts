from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    left_id = models.IntegerField()
    right_id = models.IntegerField()

    def __unicode__(self):
        return self.name


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