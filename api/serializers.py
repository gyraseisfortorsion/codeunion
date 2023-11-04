from rest_framework import serializers
from api.models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    rate = serializers.FloatField()  
    class Meta:
        model = Currency
        fields = '__all__'