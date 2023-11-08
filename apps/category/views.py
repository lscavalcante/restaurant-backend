from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.category.models import Category
from apps.category.serializers.category_list_response import CategoryListResponse


class CategoryAPI(ModelViewSet):
    queryset = Category.objects.filter(deleted=False)
    serializer_class = CategoryListResponse
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
