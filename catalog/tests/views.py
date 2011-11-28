from django.test import TestCase


class CatalogViewsTestCase(TestCase):
    fixtures = ['catalog_views_testdata.json']

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('collections' in resp.context)
        self.assertEqual([collection.pk for collection in resp.context['collections']], [1, 2])

        collection = resp.context['collections'][0]
        self.assertEqual(collection.name, 'The Spiral')
        self.assertEqual(collection.shirt_set.count(), 2)

        shirt = collection.shirt_set.all()
        self.assertEqual(shirt[0].name, '2006')
        self.assertEqual(shirt[1].name, '2007')

    def test_collection(self):
        resp = self.client.get('/thisshouldfail404/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/the_spiral/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('collection' in resp.context)

        collection = resp.context['collection']
        self.assertEqual(collection.pk, 1)
        self.assertEqual(collection.name, 'The Spiral')        

    def test_shirt(self):
        resp = self.client.get('/the_spiral/thisshouldfail404/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/thisshouldfail404/2006/')
        self.assertEqual(resp.status_code, 404)

        resp = self.client.get('/the_spiral/2006/')
        self.assertTrue(resp.status_code, 200)
        self.assertTrue('shirt' in resp.context)

        shirt = resp.context['shirt']
        self.assertEqual(shirt.pk, 1)
        self.assertEqual(shirt.name, '2006')