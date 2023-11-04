from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Currency

class CurrencyTests(APITestCase):
    def setUp(self):
        self.currency = Currency.objects.create(name='USD', rate=500)

    def test_get_currency_list(self):
        url = reverse('currency-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_currency_detail(self):
        url = reverse('currency-detail', kwargs={'pk': self.currency.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.currency.name)
        self.assertEqual(response.data['rate'], self.currency.rate)

    def test_authentication(self):
        url = reverse('currency-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
