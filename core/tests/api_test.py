from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from core import models

class BanksVSTestCase(APITestCase):
    def setUp(self):
        self.bank = models.Bank.objects.create(name='Банк 1', address='ул. Рихарда Зорге, 45')

    def test_create(self):
        data = {'name': 'Банк 2', 'address': 'ул. Рихарда Зорге, 44'}
        url = reverse('banks-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        url = reverse('banks-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        bank_id = 1
        url = reverse('banks-detail', args=[bank_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        bank_id = 1
        url = reverse('banks-detail', args=[bank_id])
        data = {'name': 'Банк 22', 'address': 'ул. Рихарда Зорге, 45'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        bank_id = 1
        url = reverse('banks-detail', args=[bank_id])
        data = {'name': 'Банк 3'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        bank_id = 1
        url = reverse('banks-detail', args=[bank_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
