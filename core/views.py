from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models

def renderDate(request):
    now = datetime.now()
    date = now.strftime("%d.%m.%Y")
    return render(request, 'core/index.html', {'date': date, 'title': 'Текущая дата'})

def renderBanks(request):
    banks = models.Bank.objects.all()
    return render(request, 'core/index.html', {'banks': banks, 'title': 'Список банков'})

def renderCurrency(request):
    currency = models.Currency.objects.all()
    return render(request, 'core/currency.html', {'currency': currency, 'title': 'Список валют'})

def renderDepositors(request):
    depositors = models.Depositor.objects.all()
    return render(request, 'core/depositors.html', {'depositors': depositors, 'title': 'Список вкладчиков'})

def renderDeposits(request):
    deposits = models.Deposit.objects.all()
    return render(request, 'core/deposits.html', {'deposits': deposits, 'title': 'Список вкладов'})