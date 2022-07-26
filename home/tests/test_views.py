from django.test import TestCase,Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index:index')
        self.paginated_product_view = reverse('index:paginated_product_view')


    def test_index_GET(self):
        response = self.client.get(self.index)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.html')

    """def test_product_POST(self):
        response = self.client.post()"""