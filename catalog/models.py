from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

class Shirt(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

