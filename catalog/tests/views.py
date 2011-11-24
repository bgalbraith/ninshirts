from django.core.urlresolvers import reverse
from django.test import TestCase


class CatalogViewsTestCase(TestCase):
    fixtures = ['catalog_views_testdata.json']

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('collections' in resp.context)
        self.assertEqual([collection.pk for collection in resp.context['collections']], [1])

    def test_collection(self):
        resp = self.client.get('/the_spiral')
        self.assertEqual(resp.status_code, 200)
