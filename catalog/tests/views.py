from django.test import TestCase


class CatalogViewsTestCase(TestCase):
    fixtures = ['catalog_views_testdata.json']

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('categories' in resp.context)
        self.assertEqual([category.pk for category in resp.context['categories']], [1, 2])

        category = resp.context['categories'][0]
        self.assertEqual(category.name, 'The Spiral')
        self.assertEqual(category.product_set.count(), 2)

        product = category.product_set.all()
        self.assertEqual(product[0].name, '2006')
        self.assertEqual(product[1].name, '2007')

    def test_category(self):
        resp = self.client.get('/thisshouldfail404/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/the_spiral/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('category' in resp.context)

        category = resp.context['category']
        self.assertEqual(category.pk, 1)
        self.assertEqual(category.name, 'The Spiral')        

    def test_product(self):
        resp = self.client.get('/the_spiral/thisshouldfail404/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/thisshouldfail404/2006/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/the_spiral/2006/')
        self.assertTrue(resp.status_code, 200)
        self.assertTrue('product' in resp.context)

        product = resp.context['product']
        self.assertEqual(product.pk, 1)
        self.assertEqual(product.name, '2006')