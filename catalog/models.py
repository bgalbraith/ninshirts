from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Shirt(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    front = models.ImageField(upload_to='shirts', blank=True)
    back = models.ImageField(upload_to='shirts', blank=True)

    def __unicode__(self):
        return self.name