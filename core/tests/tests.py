from django.test import TestCase, Client
from core import models
from django.utils import timezone

class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.bank = models.Bank.objects.create(
            name='ПАО "СтандартБанк"',
            address='ул. Карла Маркса, 12/3',
        )
        self.currency = models.Currency.objects.create(
            code='KZT',
            name='Тенге',
        )
        self.depositor = models.Depositor.objects.create(
            last_name='Петров',
            first_name='Василий',
            patronymic='Абрамович',
            role='depositorNormal',
            email='petrov_vas@mail.ru',
            telephone='+78145267253',
            bank=self.bank,
            photo='',
            passport='2457 145780',
        )
        self.deposit = models.Deposit.objects.create(
            amount=234567,
            depositor=self.depositor,
            currency=self.currency,
            annual_percentage=5,
        )

    def test_bank_detail(self):
        response = self.client.get(f'/bank/{self.bank.id}')
        self.assertEqual(response.status_code, 200)

    def test_currency_detail(self):
        response = self.client.get(f'/currency/{self.currency.id}')
        self.assertEqual(response.status_code, 200)

    def test_depositor_detail(self):
        response = self.client.get(f'/depositor/{self.depositor.id}')
        self.assertEqual(response.status_code, 200)

    def test_deposit_detail(self):
        response = self.client.get(f'/deposit/{self.deposit.id}')
        self.assertEqual(response.status_code, 200)

    def test_banks(self):
        name = 'о'
        response = self.client.get(f'/banks/{name}')
        self.assertEqual(response.status_code, 200)

    def test_currency(self):
        name = 'р'
        response = self.client.get(f'/currency/{name}')
        self.assertEqual(response.status_code, 200)

    def test_depositors(self):
        role = 'depositorNormal'
        response = self.client.get(f'/depositors/role/{role}')
        self.assertEqual(response.status_code, 200)

    def test_deposits(self):
        depositor_id = 1
        response = self.client.get(f'/deposits/depositor/{depositor_id}')
        self.assertEqual(response.status_code, 200)

    def test_admin_redirect(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

