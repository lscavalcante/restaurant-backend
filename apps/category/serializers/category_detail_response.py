from rest_framework.serializers import ModelSerializer

from apps.category.models import Category


class CategoryDetailResponse(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
