from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from core import models, filters, serializers

class BanksList(ListView):
    model = models.Bank
    context_object_name = 'banks'
    template_name = 'core/index.html'

    def get_filters(self):
        queryset = super().get_queryset()
        return filters.BanksFilter(self.request.GET, queryset=queryset)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.get_filters()
        context['title'] = 'Список банков'
        return context

class CurrencyList(ListView):
    model = models.Currency
    template_name = 'core/currency.html'
    context_object_name = 'currency'

    def get_filters(self):
        queryset = super().get_queryset()
        return filters.CurrencyFilter(self.request.GET, queryset=queryset)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.get_filters()
        context['title'] = 'Список валют'
        return context

class DepositorsList(ListView):
    model = models.Depositor
    template_name = 'core/depositors.html'
    context_object_name = 'depositors'

    def get_filters(self):
        queryset = super().get_queryset()
        return filters.DepositorFilter(self.request.GET, queryset=queryset)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.get_filters()
        context['title'] = 'Список кладчиков'
        context['roles'] = ['depositorPremium', 'depositorNormal', 'depositorGarbage']
        return context

class DepositsList(ListView):
    model = models.Deposit
    template_name = 'core/deposits.html'
    context_object_name = 'deposits'

    def get_filters(self):
        queryset = super().get_queryset()
        return filters.DepositFilter(self.request.GET, queryset=queryset)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filters'] = self.get_filters()
        context['title'] = 'Список кладов'
        context['depositors'] = models.Depositor.objects.all()
        return context

class BankView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.kwargs['name']
        banks = models.Bank.objects.filter(name__icontains=name)
        context['banks'] = banks
        context['name'] = name
        context['title'] = 'Банки'
        return context

class CurrencyView(TemplateView):
    template_name = 'core/currency.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.kwargs['name']
        currency = models.Currency.objects.filter(name__icontains=name)
        context['currency'] = currency
        context['name'] = name
        context['title'] = 'Валюты'
        return context

class DepositView(TemplateView):
    template_name = 'core/deposits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        depositor_id = self.kwargs['depositor_id']
        deposits = models.Deposit.objects.filter(depositor=depositor_id)
        depositors = models.Depositor.objects.all()
        depositor = models.Depositor.objects.get(pk=depositor_id)
        context['deposits'] = deposits
        context['depositors'] = depositors
        context['depositor'] = depositor
        context['title'] = 'Вклады: '
        return context

class DepositorView(ListView):
    template_name = 'core/depositors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        role = self.kwargs['role']
        depositors = models.Depositor.objects.filter(role__icontains=role)
        context['depositors'] = depositors
        context['role'] = role
        context['title'] = 'Вклачики '
        return context

class BankDetail(DetailView):
    model = models.Bank
    context_object_name = 'bank'
    template_name = 'core/bank_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_info'] = 'пн-пт с 10:00 до 20:00, сб-вс c 10:00 до 17:00'
        context['title'] = 'Банк'
        return context

class CurrencyDetail(DetailView):
    model = models.Currency
    context_object_name = 'currency'
    template_name = 'core/currency_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_info'] = 'подлежит обмену'
        context['title'] = 'Валюта'
        return context

class DepositorDetail(DetailView):
    model = models.Depositor
    context_object_name = 'depositor'
    template_name = 'core/depositor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вкладчик'
        return context

class DepositDetail(DetailView):
    model = models.Deposit
    context_object_name = 'deposit'
    template_name = 'core/deposit_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вклад'
        return context

class RedirectAdmin(RedirectView):
    query_string = True
    url = 'http://127.0.0.1:8000/admin/'

class BanksVS(ModelViewSet):
    queryset = models.Bank.objects.all()
    filterset_class = filters.BanksFilter
    serializer_class = serializers.Banks

class BanksAPI(APIView):
    def get(self, request):
        qs = models.Bank.objects.all()
        names = [p.name for p in qs]
        serializer = serializers.Banks(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Banks(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})

    def patch(self, request):
        bank_id = request.data.get('id')
        try:
            bank = models.Bank.objects.get(id=bank_id)
        except models.Bank.DoesNotExist:
            return Response({'message': 'Bank not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Banks(instance=bank, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Bank updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        bank_id = request.data.get('id')
        try:
            bank = models.Bank.objects.get(id=bank_id)
        except models.Bank.DoesNotExist:
            return Response({'message': 'Bank not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Banks(instance=bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Bank updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        bank_id = request.data.get('id')
        try:
            bank = models.Bank.objects.get(id=bank_id)
        except models.Bank.DoesNotExist:
            return Response({'message': 'Bank not found'}, status=status.HTTP_404_NOT_FOUND)

        bank.delete()
        return Response({'message': 'Bank deleted'})

class CurrencyAPI(APIView):
    def get(self, request):
        qs = models.Currency.objects.all()
        names = [p.name for p in qs]
        serializer = serializers.Currency(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Currency(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})

    def patch(self, request):
        currency_id = request.data.get('id')
        try:
            currency = models.Currency.objects.get(id=currency_id)
        except models.Currency.DoesNotExist:
            return Response({'message': 'Currency not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Currency(instance=currency, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Currency updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        currency_id = request.data.get('id')
        try:
            currency = models.Currency.objects.get(id=currency_id)
        except models.Currency.DoesNotExist:
            return Response({'message': 'Currency not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Currency(instance=currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Currency updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        currency_id = request.data.get('id')
        try:
            currency = models.Currency.objects.get(id=currency_id)
        except models.Currency.DoesNotExist:
            return Response({'message': 'Currency not found'}, status=status.HTTP_404_NOT_FOUND)

        currency.delete()
        return Response({'message': 'Currency deleted'})

class DepositorsAPI(APIView):
    def get(self, request):
        qs = models.Depositor.objects.all()
        serializer = serializers.Depositors(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Depositors(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})

    def patch(self, request):
        depositor_id = request.data.get('id')
        try:
            depositor = models.Depositor.objects.get(id=depositor_id)
        except models.Depositor.DoesNotExist:
            return Response({'message': 'Depositor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Depositors(instance=depositor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Depositor updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        depositor_id = request.data.get('id')
        try:
            depositor = models.Depositor.objects.get(id=depositor_id)
        except models.Depositor.DoesNotExist:
            return Response({'message': 'Depositor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Depositors(instance=depositor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Depositor updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        depositor_id = request.data.get('id')
        try:
            depositor = models.Depositor.objects.get(id=depositor_id)
        except models.Depositor.DoesNotExist:
            return Response({'message': 'Depositor not found'}, status=status.HTTP_404_NOT_FOUND)

        depositor.delete()
        return Response({'message': 'Depositor deleted'})

class DepositsAPI(APIView):
    def get(self, request):
        qs = models.Deposit.objects.all()
        serializer = serializers.Deposits(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.Deposits(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'OK'})

    def patch(self, request):
        deposit_id = request.data.get('id')
        try:
            deposit = models.Deposit.objects.get(id=deposit_id)
        except models.Deposit.DoesNotExist:
            return Response({'message': 'Deposit not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Deposits(instance=deposit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Deposit updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        deposit_id = request.data.get('id')
        try:
            deposit = models.Deposit.objects.get(id=deposit_id)
        except models.Deposit.DoesNotExist:
            return Response({'message': 'Deposit not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.Deposits(instance=deposit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Deposit updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        deposit_id = request.data.get('id')
        try:
            deposit = models.Deposit.objects.get(id=deposit_id)
        except models.Deposit.DoesNotExist:
            return Response({'message': 'Deposit not found'}, status=status.HTTP_404_NOT_FOUND)

        deposit.delete()
        return Response({'message': 'Deposit deleted'})
