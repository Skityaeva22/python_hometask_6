from datetime import date
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Bank(models.Model):
    name = models.CharField('Наименование', max_length=100, unique=True)
    address = models.CharField('Адрес', max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Bank', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

class Currency(models.Model):
    code = models.CharField('Кодовой обозначение', max_length=5, unique=True)
    name = models.CharField('Наименование', max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Currency', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

class Depositor(models.Model):
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    role_choices = [
        ('depositorPremium', 'Вкладчик с высоким рейтингом'),
        ('depositorNormal', 'Вкладчик с обычным рейтингом'),
        ('depositorGarbage', 'Вкладчик из черного списка'),
    ]
    email = models.CharField('Почта', max_length=50, blank=True)
    telephone = models.CharField('Телефон', max_length=12, blank=True)
    role = models.CharField('Роль', max_length=20, choices=role_choices)
    birthday = models.DateField('День рождения', null=True, blank=True, default=timezone.now)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name='Банк')
    photo = models.ImageField('Фото вкладчика', upload_to='photos', null=True, blank=True)
    passport = models.CharField('Серия и номер паспорта', max_length=11, default='', unique=True)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('Depositor', kwargs={'pk': self.pk})

    def get_full_name(self) -> str:
        first_name = self.first_name
        last_name = self.last_name
        patronymic = self.patronymic

        if first_name:
            return f"{first_name} {last_name} {patronymic}".strip()
        elif last_name:
            return last_name
        else:
            return 'нет данных'
    class Meta:
        verbose_name = 'Вкладчик'
        verbose_name_plural = 'Вкладчики'

class Deposit(models.Model):
    amount = models.DecimalField('Сумма', default=0.00, max_digits=10, decimal_places=2)
    depositor = models.ForeignKey(Depositor, on_delete=models.CASCADE, verbose_name='Вкладчик')
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, verbose_name='Валюта')
    annual_percentage = models.DecimalField('Годовой процент', default=0.00, max_digits=5, decimal_places=2)
    dc = models.DateTimeField('Дата записи', null=True, blank=True, default=timezone.now)

    def __str__(self):
        return f"{self.depositor} - {self.amount} {self.currency.code}"

    def get_absolute_url(self):
        return reverse('Deposit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Вклад'
        verbose_name_plural = 'Вклады'
