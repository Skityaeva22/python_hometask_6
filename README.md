1) In [2]: models.Bank.objects.all()
Out[2]: <QuerySet [<Bank: ООО "Рога и Копыта">, <Bank: ООО "Зеленоглазое такси">, <Bank: ООО "Спербанк">, <Bank: ПАО "Ромашка">]>

2) In [7]: models.Bank.objects.order_by('name')
Out[7]: <QuerySet [<Bank: ООО "Зеленоглазое такси">, <Bank: ООО "Рога и Копыта">, <Bank: ООО "Спербанк">, <Bank: ПАО "Ромашка">]>

3) In [8]: models.Bank.objects.order_by('-name')
Out[8]: <QuerySet [<Bank: ПАО "Ромашка">, <Bank: ООО "Спербанк">, <Bank: ООО "Рога и Копыта">, <Bank: ООО "Зеленоглазое такси">]>

4) In [9]: models.Bank.objects.order_by('address')
Out[9]: <QuerySet [<Bank: ПАО "Ромашка">, <Bank: ООО "Спербанк">, <Bank: ООО "Рога и Копыта">, <Bank: ООО "Зеленоглазое такси">]>

5) In [10]: models.Bank.objects.order_by('-address')
Out[10]: <QuerySet [<Bank: ООО "Зеленоглазое такси">, <Bank: ООО "Рога и Копыта">, <Bank: ООО "Спербанк">, <Bank: ПАО "Ромашка">]>

6) In [11]: models.Bank.objects.filter(name__contains='м')
Out[11]: <QuerySet [<Bank: ПАО "Ромашка">]>

7) In [12]: models.Bank.objects.filter(name__exact='ПАО "Ромашка"')
Out[12]: <QuerySet [<Bank: ПАО "Ромашка">]>

8) In [15]: models.Bank.objects.filter(address__icontains='Карла')
Out[15]: <QuerySet [<Bank: ООО "Рога и Копыта">, <Bank: ООО "Зеленоглазое такси">, <Bank: ООО "Спербанк">, <Bank: ПАО "Ромашка">]>

9) In [16]: models.Bank.objects.filter(address__exact='Карла Маркса, 12/6')
Out[16]: <QuerySet []>

10) In [19]: models.Currency.objects.all()
Out[19]: <QuerySet [<Currency: Рубль>, <Currency: Доллар>, <Currency: Евро>, <Currency: Фунт>]>

11) In [20]: models.Currency.objects.order_by('code')
Out[20]: <QuerySet [<Currency: Доллар>, <Currency: Евро>, <Currency: Рубль>, <Currency: Фунт>]>

12) In [21]: models.Currency.objects.order_by('-code')
Out[21]: <QuerySet [<Currency: Фунт>, <Currency: Рубль>, <Currency: Евро>, <Currency: Доллар>]>

13) In [22]: models.Currency.objects.order_by('name')
Out[22]: <QuerySet [<Currency: Доллар>, <Currency: Евро>, <Currency: Рубль>, <Currency: Фунт>]>

14) In [23]: models.Currency.objects.order_by('-name')
Out[23]: <QuerySet [<Currency: Фунт>, <Currency: Рубль>, <Currency: Евро>, <Currency: Доллар>]>

15) In [26]: models.Currency.objects.filter(name__contains='о')
Out[26]: <QuerySet [<Currency: Доллар>, <Currency: Евро>]>

16) In [27]: models.Currency.objects.filter(name__exact='Рубль')
Out[27]: <QuerySet [<Currency: Рубль>]>

17) In [28]: models.Currency.objects.filter(code__icontains='р')
Out[28]: <QuerySet [<Currency: Рубль>]>

18) In [29]: models.Currency.objects.filter(code__exact='руб.')
Out[29]: <QuerySet [<Currency: Рубль>]>

19) In [30]: models.Depositor.objects.all()
Out[30]: <QuerySet [<Depositor: Иван Иванов Иванович>, <Depositor: Петр Петров>, <Depositor: Никита Никитин>, <Depositor: Семен Сидоров>]>

20) In [31]: models.Depositor.objects.filter(birthday__year=2000)
Out[31]: <QuerySet [<Depositor: Иван Иванов Иванович>, <Depositor: Петр Петров>]>

21) In [35]: models.Depositor.objects.filter(birthday__year=2000).order_by('-first_name')
Out[35]: <QuerySet [<Depositor: Петр Петров>, <Depositor: Иван Иванов Иванович>]>

22) In [36]: models.Depositor.objects.latest('birthday')
Out[36]: <Depositor: Семен Сидоров>

23) In [37]: models.Depositor.objects.filter(birthday__day=12)
Out[37]: <QuerySet [<Depositor: Иван Иванов Иванович>, <Depositor: Петр Петров>, <Depositor: Семен Сидоров>]>

24) In [41]: models.Depositor.objects.filter(birthday__month=1)
Out[41]: <QuerySet [<Depositor: Петр Петров>]>

25) In [42]: models.Deposit.objects.all()
Out[42]: <QuerySet [<Deposit: Иван Иванов Иванович - 1000000.00 руб.>, <Deposit: Петр Петров - 2000.00 $>, <Deposit: Никита Никитин - 10000.00 eu>]>

26) In [43]: models.Deposit.objects.filter(amount__gt=2000)
Out[43]: <QuerySet [<Deposit: Иван Иванов Иванович - 1000000.00 руб.>, <Deposit: Никита Никитин - 10000.00 eu>]>

27) In [45]: models.Deposit.objects.filter(amount__lt=10000)
Out[45]: <QuerySet [<Deposit: Петр Петров - 2000.00 $>]>

28) In [46]: models.Deposit.objects.filter(amount__lte=10000)
Out[46]: <QuerySet [<Deposit: Петр Петров - 2000.00 $>, <Deposit: Никита Никитин - 10000.00 eu>]>

29) In [47]: models.Deposit.objects.filter(amount__gte=10000)
Out[47]: <QuerySet [<Deposit: Иван Иванов Иванович - 1000000.00 руб.>, <Deposit: Никита Никитин - 10000.00 eu>]>

30) In [48]: models.Depositor.objects.dates('birthday', 'day')
Out[48]: <QuerySet [datetime.date(1999, 10, 1), datetime.date(2000, 1, 12), datetime.date(2000, 5, 12), datetime.date(2002, 5, 12)]>

31) In [50]: models.Depositor.objects.dates('birthday', 'day').reverse()
Out[50]: <QuerySet [datetime.date(2002, 5, 12), datetime.date(2000, 5, 12), datetime.date(2000, 1, 12), datetime.date(1999, 10, 1)]>

32) In [51]: models.Depositor.objects.values('last_name', 'passport', 'bank', 'role')
Out[51]: <QuerySet [{'last_name': 'Иванов', 'passport': '3333 333333', 'bank': 1, 'role': 'depositorPremium'}, {'last_name': 'Петров', 'passport': '2222 222222', 'bank': 2, 'role':
 'depositorNormal'}, {'last_name': 'Никитин', 'passport': '1111 111111', 'bank': 3, 'role': 'depositorGarbage'}, {'last_name': 'Сидоров', 'passport': '1111 111112', 'bank': 1, 'role': 'depositorNormal'}]>

33) In [61]: models.Depositor.objects.exclude(first_name__contains='И')
Out[61]: <QuerySet [<Depositor: Петр Петров>, <Depositor: Никита Никитин>, <Depositor: Семен Сидоров>]>

34) In [62]: models.Depositor.objects.values_list('patronymic', flat=True)
Out[62]: <QuerySet ['Иванович', '', '', '']>

35) In [65]: models.Deposit.objects.values('dc', 'amount', 'depositor')
Out[65]: <QuerySet [{'dc': datetime.datetime(2024, 5, 12, 9, 52, 40, tzinfo=datetime.timezone.utc), 'amount': Decimal('1000000.00'), 'depositor': 1}, {'dc': datetime.datetime(2024,
 5, 12, 9, 53, 9, tzinfo=datetime.timezone.utc), 'amount': Decimal('2000.00'), 'depositor': 2}, {'dc': datetime.datetime(2024, 5, 12, 9, 53, 21, tzinfo=datetime.timezone.utc), 'amount': Decimal('10000.00'), 'depositor': 3}]>

36) In [66]: models.Deposit.objects.values('depositor', 'amount', 'currency').filter(amount__lte=9999).reverse()
Out[66]: <QuerySet [{'depositor': 2, 'amount': Decimal('2000.00'), 'currency': 2}]>

37) In [67]: models.Deposit.objects.values('depositor', 'amount', 'currency', 'annual_percentage').filter(amount__gte=10000)
Out[67]: <QuerySet [{'depositor': 1, 'amount': Decimal('1000000.00'), 'currency': 1, 'annual_percentage': Decimal('10.06')}, {'depositor': 3, 'amount': Decimal('10000.00'), 'currency': 3, 'annual_percentage': Decimal('5.00')}]>

38) In [68]: models.Deposit.objects.latest('dc')
Out[68]: <Deposit: Никита Никитин - 10000.00 eu>

39) In [71]: models.Deposit.objects.filter(dc__year=2024)
Out[71]: <QuerySet [<Deposit: Иван Иванов Иванович - 1000000.00 руб.>, <Deposit: Петр Петров - 2000.00 $>, <Deposit: Никита Никитин - 10000.00 eu>]>

40) In [75]: models.Depositor.objects.values('first_name', 'last_name').filter(birthday__year__lte=1999).reverse()
Out[75]: <QuerySet [{'first_name': 'Никита', 'last_name': 'Никитин'}]>


Ранее использовавшиеся модели:
# def renderDate(request):
#     now = datetime.now()
#     date = now.strftime("%d.%m.%Y")
#     return render(request, 'core/index.html', {'date': date, 'title': 'Текущая дата'})
#
# def renderBanks(request):
#     banks = models.Bank.objects.all()
#     return render(request, 'core/index.html', {'banks': banks, 'title': 'Список банков'})
#
# def renderCurrency(request):
#     currency = models.Currency.objects.all()
#     return render(request, 'core/currency.html', {'currency': currency, 'title': 'Список валют'})
#
# def renderDepositors(request):
#     depositors = models.Depositor.objects.all()
#     return render(request, 'core/depositors.html', {'depositors': depositors, 'title': 'Список вкладчиков'})
#
# def renderDeposits(request):
#     deposits = models.Deposit.objects.all()
#     depositors = models.Depositor.objects.all()
#     context = {
#         'deposits': deposits,
#         'depositors': depositors,
#         'title': 'Список вкладов'
#     }
#     return render(request, template_name='core/deposits.html', context=context)
#
# def get_deposit(request, depositor_id):
#     deposits = models.Deposit.objects.filter(depositor=depositor_id)
#     depositors = models.Depositor.objects.all()
#     depositor = models.Depositor.objects.get(pk=depositor_id)
#     context = {
#         'deposits': deposits,
#         'depositors': depositors,
#         'depositor': depositor,
#         'title': 'Вклады: '
#     }
#     return render(request, template_name='core/deposits.html', context=context)
#
# def get_depositor(request, role):
#     depositors = models.Depositor.objects.filter(role=role)
#     role = role
#     context = {
#         'depositors': depositors,
#         'role': role,
#         'title': 'Вклачики '
#     }
#     return render(request, template_name='core/depositors.html', context=context)
#
# def get_currency(request, name):
#     currency = models.Currency.objects.filter(name__icontains=name)
#     name = name
#     context = {
#         'currency': currency,
#         'name': name,
#         'title': 'Валюты'
#     }
#     return render(request, template_name='core/currency.html', context=context)
#
# def get_bank(request, name):
#     banks = models.Bank.objects.filter(name__icontains=name)
#     name = name
#     context = {
#         'banks': banks,
#         'name': name,
#         'title': 'Банки'
#     }
#     return render(request, template_name='core/index.html', context=context)
