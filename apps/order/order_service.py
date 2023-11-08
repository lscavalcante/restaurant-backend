from apps.item.models import Item
from apps.order.models import Order, OrderItem


class OrderService:

    @classmethod
    def create_order(cls, create_order_request, user) -> Order:
        items = create_order_request.validated_data.pop('items')
        order = Order.objects.create(**create_order_request.validated_data)

        if user.is_authenticated:
            order.user_id = user.id
            order.save()

        for item in items:
            founded_item = Item.objects.filter(id=item.get('id')).first()
            if founded_item:
                OrderItem.objects.create(
                    order=order,
                    item=founded_item,
                    price=founded_item.price,
                    quantity=item.get('quantity')
                )

        return order
