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
    depositors = models.Depositor.objects.all()
    context = {
        'deposits': deposits,
        'depositors': depositors,
        'title': 'Список вкладов'
    }
    return render(request, template_name='core/deposits.html', context=context)

def get_depositor(request, depositor_id):
    deposits = models.Deposit.objects.filter(depositor=depositor_id)
    depositors = models.Depositor.objects.all()
    depositor = models.Depositor.objects.get(pk=depositor_id)
    context = {
        'deposits': deposits,
        'depositors': depositors,
        'depositor': depositor,
        'title': 'Вклады: '
    }
    return render(request, template_name='core/deposits.html', context=context)