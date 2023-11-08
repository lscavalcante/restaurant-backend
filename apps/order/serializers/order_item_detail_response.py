from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.order.models import OrderItem


class OrderDetailResponse(ModelSerializer):
    item_name = serializers.CharField(source='get_item_name')
    item_image = serializers.CharField(source='get_item_name')

    class Meta:
        model = OrderItem
        fields = '__all__'
