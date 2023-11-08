from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import filters, status

from apps.category.models import Category
from apps.item.filters.item_filter import ItemFilter
from apps.item.models import Item
from apps.item.serializers.item_create_request import ItemCreateRequest
from apps.item.serializers.item_detail_response import ItemDetailResponse
from apps.item.serializers.item_list_response import ItemListResponse
from apps.item.serializers.recommended_items_response import RecommendedItemsResponse


class ItemAPI(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemListResponse
    parser_classes = [MultiPartParser, JSONParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    filterset_class = ItemFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["name", "category__name"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ItemListResponse(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ItemListResponse(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ItemCreateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = Category.objects.get(id=serializer.validated_data.pop('category_id', None))

        item = Item.objects.create(
            category_id=category.id,
            **serializer.validated_data
        )

        return Response(ItemDetailResponse(instance=item).data, status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False, url_path='recommended-items', serializer_class=RecommendedItemsResponse)
    def list_recommended_items(self, request):
        liked_items = Item.objects.all()
        recommended_items = Item.objects.all()

        foods = {
            'liked_items': liked_items,
            'recommended_items': recommended_items
        }

        data = RecommendedItemsResponse(instance=foods).data

        return Response(data, 200)
