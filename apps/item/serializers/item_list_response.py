from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.item.models import Item


class ItemListResponse(ModelSerializer):
    category_name = serializers.CharField(source='get_category_name')

    class Meta:
        model = Item
        exclude = ['created_at', 'updated_at', 'deleted']
