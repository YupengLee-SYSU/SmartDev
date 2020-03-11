from .models import StockBasic
from .models import DailyLine
from rest_framework import serializers


class StockBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockBasic
        fields = '__all__'

class DailyLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLine
        fields = '__all__'
