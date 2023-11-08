from rest_framework import serializers

from apps.item.serializers.item_list_response import ItemListResponse


class RecommendedItemsResponse(serializers.Serializer):
    liked_items = ItemListResponse(many=True)
    recommended_items = ItemListResponse(many=True)
