from rest_framework import serializers


class AddItemRequest(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    observation = serializers.CharField(allow_blank=True, allow_null=True, default="")
