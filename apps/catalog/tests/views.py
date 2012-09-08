from django.test import TestCase


class CatalogViewsTestCase(TestCase):
    fixtures = ['catalog_testdata.yaml']

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_category(self):
        resp = self.client.get('/invalid-category/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/apparel/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('category' in resp.context)

        category = resp.context['category']
        self.assertEqual(category.pk, 1)
        self.assertEqual(category.name, 'Apparel')

    def test_product(self):
        resp = self.client.get('/invalid-category/invalid-product/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/apparel/invalid-product/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get(
            '/invalid-category/4-of-us-are-dying-mens-t-shirt/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/apparel/4-of-us-are-dying-mens-t-shirt/')
        self.assertTrue(resp.status_code, 200)
        self.assertTrue('product' in resp.context)

        product = resp.context['product']
        self.assertEqual(product.pk, 1)
        self.assertEqual(product.name, "4 Of Us Are Dying Men's T-Shirt")