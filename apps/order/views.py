from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.item.models import Item
from apps.order.models import Order, OrderItem
from apps.order.order_service import OrderService
from apps.order.serializers.add_item_request import AddItemRequest
from apps.order.serializers.create_order_request import CreateItemRequest, CreateOrderRequest
from apps.order.serializers.order_detail_response import OrderDetailResponse
from apps.order.serializers.order_list_response import OrderListResponse


class OrderAPI(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListResponse
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = OrderListResponse(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = OrderListResponse(queryset, many=True)
            return Response(serializer.data)
        except Exception as ex:
            raise ex

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderDetailResponse(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = CreateOrderRequest(data=request.data)
        data.is_valid(raise_exception=True)

        new_order = OrderService.create_order(data, request.user)

        return Response({'message': f'created with success {new_order.id}'})

    @action(methods=['POST'], detail=True, url_path='add-item', serializer_class=AddItemRequest)
    def add_item(self, request, pk=None):

        data = AddItemRequest(data=request.data)
        data.is_valid(raise_exception=True)

        order = Order.objects.get(pk=pk)
        item = Item.objects.get(pk=data.validated_data.get('item_id'))

        order_item = OrderItem.objects.create(
            order_id=order.id,
            item_id=item.id,
            quantity=data.validated_data.get('quantity'),
            price=item.price
        )

        return Response({'message': 'Success'}, 201)
