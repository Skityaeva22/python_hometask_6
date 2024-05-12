# Generated by Django 5.0.6 on 2024-05-12 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_deposit_amount_alter_deposit_annual_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency', verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='depositor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.depositor', verbose_name='Вкладчик'),
        ),
        migrations.AlterField(
            model_name='depositor',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bank', verbose_name='Банк'),
        ),
    ]