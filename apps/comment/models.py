from django.db import models

from apps.item.models import Item
from apps.user.models import User
from shared.abstract_class.audited_abstract import AuditedAbstract


class Comment(AuditedAbstract):
    description = models.TextField()
    rating = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Model:
        db_table = "comments"
