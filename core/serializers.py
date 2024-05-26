from rest_framework import serializers
from core import models

class Banks(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = '__all__'

class Currency(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = '__all__'

class Depositors(serializers.ModelSerializer):
    class Meta:
        model = models.Depositor
        fields = '__all__'

class Deposits(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = '__all__'
