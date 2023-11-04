from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Currency
from decouple import config

class CurrencyTests(APITestCase):
    def setUp(self):
        self.currency = Currency.objects.create(name='USD', rate=500)
        self.currency = Currency.objects.create(name='EUR', rate=550)

    def test_get_currency_list(self):
        url = reverse('currency-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_currency_detail(self):
        url = reverse('currency-detail', kwargs={'pk': self.currency.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_currency_list(self):
        # Obtain the access token
        obtain_token_url = reverse('token_obtain_pair')
        response = self.client.post(obtain_token_url, {'username': config('ADMIN_USER'), 'password': config('ADMIN_PASSWORD')})
        print(response.data)
        access_token = response.data['access']
        
        # Use the access token for authentication
        url = reverse('currency-list')
        headers = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_authenticated_currency_detail(self):
        # Obtain the access token
        obtain_token_url = reverse('token_obtain_pair')
        response = self.client.post(obtain_token_url, {"username": config('ADMIN_USER'), "password": config('ADMIN_PASSWORD')})
        print(response.data)
        access_token = response.data['access']
        
        # Use the access token for authentication
        url = reverse('currency-detail', kwargs={'pk': self.currency.pk})
        headers = {'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
        response = self.client.get(url, **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.currency.name)
        self.assertEqual(response.data['rate'], self.currency.rate)
