from django.db import models

from shared.abstract_class.audited_abstract import AuditedAbstract


class Category(AuditedAbstract):
    name = models.TextField(unique=True)

    class Model:
        db_table = "categories"

    def __str__(self):
        return self.name
