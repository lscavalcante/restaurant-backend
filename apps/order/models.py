import decimal

from django.db import models

from apps.item.models import Item
from apps.user.models import User
from shared.abstract_class.audited_abstract import AuditedAbstract


class Order(AuditedAbstract):
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    cep = models.TextField()
    city = models.TextField()
    street = models.TextField()
    number = models.TextField()
    complement = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, default=None)

    class Model:
        db_table = "orders"

    def get_total_price(self):
        order_foods: [OrderItem] = OrderItem.objects.filter(order=self.pk, deleted=False)
        total = decimal.Decimal(0.00)

        for of in order_foods:
            total = total + (of.price * of.quantity)

        return total

    def get_full_address(self):
        address = f"{self.cep} | {self.city} | {self.street} | {self.number} | {self.complement if None else ''}"

        return address

    def get_items(self):
        return self.orderitem_set.all()


class OrderItem(AuditedAbstract):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    quantity = models.IntegerField()

    class Model:
        db_table = "order_items"

    def get_item_name(self):
        return self.item.name

    def get_item_image(self):
        return self.item.image
