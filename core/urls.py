from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# пример регистрации url
router.register('', views.BanksVS, basename='banks')

# urlpatterns = []
#
# urlpatterns += router.urls

urlpatterns = [
    path('', views.BanksList.as_view(), name='home'),
    path('banks/settings', views.BanksAPI.as_view(), name='banks_settings'),
    path('admin/', views.RedirectAdmin.as_view(), name='admin'),
    path('banks/<str:name>', views.BankView.as_view(), name='bank_by_name'),
    path('bank/<int:pk>', views.BankDetail.as_view(), name='bank_detail'),
    path('currency/', views.CurrencyList.as_view(), name='currency'),
    path('currency/settings', views.CurrencyAPI.as_view(), name='currency_settings'),
    path('currency/<int:pk>', views.CurrencyDetail.as_view(), name='currency_detail'),
    path('currency/<str:name>', views.CurrencyView.as_view(), name='currency_by_name'),
    path('depositors/', views.DepositorsList.as_view(), name='depositors'),
    path('depositors/settings', views.DepositorsAPI.as_view(), name='depositors_settings'),
    path('depositor/<int:pk>', views.DepositorDetail.as_view(), name='depositor_detail'),
    path('depositors/role/<str:role>', views.DepositorView.as_view(), name='depositors_by_role'),
    path('deposits/', views.DepositsList.as_view(), name='deposits'),
    path('deposits/settings', views.DepositsAPI.as_view(), name='deposits_settings'),
    path('deposit/<int:pk>', views.DepositDetail.as_view(), name='deposit_detail'),
    path('deposits/depositor/<int:depositor_id>', views.DepositView.as_view(), name='deposits_by_depositor'),
]
