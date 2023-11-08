from django.db import models

from apps.category.models import Category
from shared.abstract_class.audited_abstract import AuditedAbstract


class Item(AuditedAbstract):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
    observation = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, upload_to='items')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None, null=True)

    class Model:
        db_table = "items"

    def get_category_name(self):
        return self.category.name
