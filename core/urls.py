from django.urls import path
from core import views

urlpatterns = [
    path('', views.renderBanks),
    path('currency/', views.renderCurrency),
    path('depositors/', views.renderDepositors),
    path('deposits/', views.renderDeposits),
    path('deposits/depositor/<int:depositor_id>', views.get_depositor),
]
