from rest_framework import serializers


class CreateItemRequest(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    observation = serializers.CharField(allow_blank=True, allow_null=True, default="")


class CreateOrderRequest(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=255)
    cep = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    number = serializers.CharField(max_length=255)
    items = CreateItemRequest(many=True, required=True)
