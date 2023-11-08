from rest_framework.serializers import ModelSerializer

from apps.category.models import Category


class CategoryListResponse(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
