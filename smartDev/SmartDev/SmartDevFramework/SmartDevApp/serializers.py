from .models import StockBasic
from rest_framework import serializers


class StockBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockBasic
        fields = '__all__'
