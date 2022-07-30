from django.test import TestCase,Client
from django.urls import reverse
from home.models import Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(category="Laptop",
        model_name="xyz",image='xyz.jpeg',specification='NONE',
        price=100)
        self.index = reverse('index:index')
        self.paginated_product_view = reverse('index:paginated_product_view',args=[self.product.model_name])
        self.search = reverse('index:search')

    def test_index_GET(self):
        response = self.client.get(self.index)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')

    def test_search_GET(self):
        response = self.client.get(self.search)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')

    def test_search_POST(self):
        response = self.client.post(self.search,{
            'searched':'MSG'
        })
        #self.assertEqual(response.status_code,200)
        self.assertEqual(response['searched'],'MSG')

    def test_paginated_product_view_GET(self):
        response = self.client.get(self.paginated_product_view)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/paginated_product.html')


    """def test_product_POST(self):
        response = self.client.post(self.paginated_product_view,{
            ''
        })"""