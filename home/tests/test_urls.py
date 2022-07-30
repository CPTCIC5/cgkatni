from django.urls import reverse,resolve
from django.test import SimpleTestCase
from home.views import index,about,contact,search,paginated_product_view
from home.models import Product,Order

product = Product.objects.create(
category='Laptop',
model_name='xyz',
specification='specs',
price = 100
)

order = Order.objects.create(
product = product,
name = 'Aryan',
address = 'Nai Basti',
phone_no = 123 ,
email = 'aryanjainak@gmail.com'
)

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index:index')
        self.assertEqual(resolve(url).func,index)

    
    def test_paginated_product_view_url(self):
        url = reverse('index:paginated_product_view',args=[product.model_name])
        self.assertEqual(resolve(url).func,paginated_product_view)

    def test_order_url(self):
        url = reverse('index:order',args=[product.model_name])
        self.assertEqual(resolve(url).func,search)
    

    def test_about_url(self):
        url = reverse('index:about')
        self.assertEqual(resolve(url).func,about)
    
    def test_contact_url(self):
        url = reverse('index:contact')
        self.assertEqual(resolve(url).func,contact)

    def test_search_url(self):
        url = reverse('index:search')
        self.assertEqual(resolve(url).func,search)