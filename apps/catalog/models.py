from django.db import models
from itertools import chain
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Category(models.Model):
    parent = models.ForeignKey('Category', null=True)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    left_id = models.IntegerField()
    right_id = models.IntegerField()

    class Meta:
        ordering = ['left_id']
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def products(self):
        """
        Returns a flat list of all products that fall within a category and
        it's children.
        """
        children = Category.objects.filter(left_id__gt=self.left_id,
                                           right_id__lt=self.right_id)
        products = [self.product_set.all()]
        for child in children:
            products.append(child.product_set.all())

        return list(chain.from_iterable(products))

    def depth(self):
        """
        Returns the depth of a category in the category hierarchy.
        """
        depth = 1
        parent = self.parent
        while parent is not None:
            depth += 1
            parent = parent.parent

        return depth

    def family(self):
        """
        Returns a flat list of the immediate children, siblings, and ancestors
        of a category.
        """

        # add children
        family = list(Category.objects.filter(parent__exact=self))
        if self.parent is None:
            family += list(Category.objects.filter(parent__exact=None))
        else:
            parent = self.parent
            while parent is not None:
                # add siblings
                family += list(Category.objects.filter(parent__exact=parent))
                # add parent
                family.append(parent)
                parent = parent.parent

        return set(family)


class OptionType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Option(models.Model):
    option_type = models.ForeignKey(OptionType)
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)

    def __unicode__(self):
        return "[%s] %s" % (self.option_type.name, self.name)

class Product(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    options = models.ManyToManyField(Option)

    def __unicode__(self):
        return self.name

    def deep_categories(self):
        """
        Returns a flat list of all the product's categories and ancestors.
        """
        categories = list(self.categories.all())
        for category in self.categories.all():
            parent = category.parent
            while parent:
                categories.append(parent)
                parent = parent.parent

        return categories

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    original = models.ImageField(upload_to='products')
    thumbnail = ImageSpecField([ResizeToFill(200,200)], format='JPEG',
        image_field='original')
    thumbnail_medium = ImageSpecField([ResizeToFill(100,100)], format='JPEG',
        image_field='original')
    thumbnail_tiny = ImageSpecField([ResizeToFill(50,50)], format='JPEG',
        image_field='original')

    class Meta:
        order_with_respect_to = 'product'

    def __unicode__(self):
        return "%s [%d]" % (self.product.name, self._order)
