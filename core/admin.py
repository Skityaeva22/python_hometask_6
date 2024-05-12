from django.contrib import admin
from core import models


@admin.register(models.Bank)
class Bank(admin.ModelAdmin):
    ('name', 'address')

@admin.register(models.Currency)
class Currency(admin.ModelAdmin):
    ('code', 'name')

@admin.register(models.Depositor)
class Depositor(admin.ModelAdmin):
    ('last_name', 'first_name', 'patronymic', 'email', 'telephone', 'role', 'bank')

@admin.register(models.Deposit)
class Deposit(admin.ModelAdmin):
    ('amount', 'depositor', 'currency', 'annual_percentage', 'dc')
