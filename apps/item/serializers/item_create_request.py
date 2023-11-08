from rest_framework import serializers


class ItemCreateRequest(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=16, decimal_places=2)
    observation = serializers.CharField(max_length=255, allow_blank=True)
    image = serializers.ImageField(required=True)
    category_id = serializers.IntegerField()
