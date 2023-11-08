from rest_framework.serializers import ModelSerializer

from apps.item.models import Item


class ItemDetailResponse(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
