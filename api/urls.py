from django.urls import path
from api.views import CurrencyList, CurrencyDetail

urlpatterns = [
    path('api/currencies/', CurrencyList.as_view(), name='currency-list'),
    path('api/currency/<int:pk>/', CurrencyDetail.as_view(), name='currency-detail'),
]