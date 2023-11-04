from django.shortcuts import render

from rest_framework import generics
from api.models import Currency
from api.serializers import CurrencySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class CurrencyList(generics.ListAPIView):
    serializer_class = CurrencySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        page = self.request.query_params.get('page')
        per_page = self.request.query_params.get('per_page')

        if page is None:
            page = 0
        else:
            page = int(page)

        if per_page is None:
            per_page = 10  # Set a default value for per_page
        else:
            per_page = int(per_page)

        queryset = Currency.objects.all()
        return queryset[page * per_page: (page + 1) * per_page]

class CurrencyDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
