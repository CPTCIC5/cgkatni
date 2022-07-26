from django.urls import reverse,resolve
from django.test import SimpleTestCase
from home.views import index,about,contact,paginated_product_view
from home.models import Product

class TestUrls(SimpleTestCase):
    """def setUp(self):
        self.product = Product.objects.create(
            category='Laptop',
            model_name='xyz',
            specification='specs',
            price = 100
        )"""

    def test_index_url(self):
        url = reverse('index:index')
        self.assertEqual(resolve(url).func,index)
    """
    def test_paginated_product_view_url(self):
        url = reverse('index:paginated_product_view',args=[self.product.model_name])
        self.assertEqual(resolve(url).func,paginated_product_view)

    def test_paginated_product_view_url(self):
        url = reverse('index:paginated_product_view',args=[self.product.model_name])
        self.assertEqual(resolve(url).func,paginated_product_view)
    """
    def test_about_url(self):
        url = reverse('index:about')
        self.assertEqual(resolve(url).func,about)
    
    def test_contact_url(self):
        url = reverse('index:contact')
        self.assertEqual(resolve(url).func,contact)