from rest_framework import serializers
from rest_framework.fields import IntegerField, CharField

from .models import Region

class RegionSerializer(serializers.ModelSerializer):
    name=CharField(max_length=255)
    class Meta:
        model = Region
        fields = ['id', 'name']

from rest_framework import serializers
from .models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'