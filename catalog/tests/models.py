from django.test import TestCase
from catalog.models import Category

class CatalogCategoryTestCase(TestCase):
    fixtures = ['catalog_views_testdata.yaml']

    def test_products(self):
        category = Category.objects.get(name='T-Shirts')
        self.assertEqual(len(category.products()), 8)

        category = Category.objects.get(name='Apparel')
        self.assertEqual(len(category.products()), 12)
