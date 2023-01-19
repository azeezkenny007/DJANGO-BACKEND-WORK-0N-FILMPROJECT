from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class MyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("successfully set the data")
        pass

    def setUp(self):
        print("set to run everytime")
        pass

    def test_check_If_the_template_is_okay(self):
        self.assertTrue(True)

    def test_if_endpoint_correct(self):
        response = self.client.get('/pages/index2/')
        self.assertEqual(response.status_code, 200)
        
    def test_if_reverse_endpoint_correct(self):
        response = self.client.get(reverse('index2'))
        self.assertEqual(response.status_code, 200)
  