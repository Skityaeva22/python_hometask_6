import django_filters
from django.db.models import Q

from core import models


class DepositorFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(field_name='role')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    patronymic = django_filters.CharFilter(field_name='patronymic', lookup_expr='icontains')

    class Meta:
        model = models.Depositor
        fields = ['role', 'last_name', 'first_name', 'patronymic']

class DepositFilter(django_filters.FilterSet):
    depositor = django_filters.CharFilter(field_name='depositor')

    class Meta:
        model = models.Deposit
        fields = ['depositor']

class CurrencyFilter(django_filters.FilterSet):
    term = django_filters.CharFilter(method='term_filter')

    class Meta:
        model = models.Currency
        fields = '__all__'

    def term_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(code__icontains=value))

class BanksFilter(django_filters.FilterSet):
    term = django_filters.CharFilter(method='term_filter')

    class Meta:
        model = models.Bank
        fields = '__all__'

    def term_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(address__icontains=value))
