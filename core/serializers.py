from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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

    def validate(self, attrs: dict):
        if attrs['amount'] < 1000:
            raise ValidationError('Сумма вклада не может быть меньше 1000')

        if attrs['annual_percentage'] < 4:
            raise ValidationError('Процент по вкладу не может быть меньше 4')

        return attrs
