from django.test import TestCase
from catalog.models import Category, Product

class CatalogCategoryTestCase(TestCase):
    fixtures = ['catalog_testdata.yaml']

    def test_products(self):
        category = Category.objects.get(name='T-Shirts')
        self.assertEqual(len(category.products()), 8)

        category = Category.objects.get(name='Apparel')
        self.assertEqual(len(category.products()), 12)

class CatalogProductTestCase(TestCase):
    fixtures = ['catalog_testdata.yaml']

    def test_deep_categories(self):
        product = Product.objects.get(name="Art Is Resistance Women's T-Shirt")
        self.assertEqual(len(product.deep_categories()), 6)

        product = Product.objects.get(name="Pretty Hate Machine 2010 Hoodie")
        self.assertEqual(len(product.deep_categories()), 5)