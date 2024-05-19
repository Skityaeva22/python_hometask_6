from django.urls import path
from core import views

urlpatterns = [
    path('', views.renderBanks, name='home'),
    path('banks/<str:name>', views.get_bank, name='bank_by_name'),
    path('currency/', views.renderCurrency, name='currency'),
    path('currency/<str:name>', views.get_currency, name='currency_by_name'),
    path('depositors/', views.renderDepositors, name='depositors'),
    path('depositors/role/<str:role>', views.get_depositor, name='depositors_by_role'),
    path('deposits/', views.renderDeposits, name='deposits'),
    path('deposits/depositor/<int:depositor_id>', views.get_deposit, name='deposits_by_depositor'),
]
