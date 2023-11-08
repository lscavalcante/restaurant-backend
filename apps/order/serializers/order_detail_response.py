from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.order.models import Order
from apps.order.serializers.order_item_detail_response import OrderDetailResponse


class OrderDetailResponse(ModelSerializer):
    total_price = serializers.DecimalField(source='get_total_price', max_digits=16, decimal_places=2)
    address = serializers.CharField(source='get_full_address')
    order_items = OrderDetailResponse(many=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = '__all__'
