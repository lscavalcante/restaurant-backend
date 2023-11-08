import os

import django
import decimal
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from apps.category.models import Category
from apps.item.models import Item
from apps.user.models import User
from faker import Faker
from faker.providers.person.pt_BR import Provider as PtBrPersonProvider
from faker.providers.python import Provider as FakerPythonProvider


def init_db():
    user1 = User.objects.create_user(email='lucasantoscv@gmail.com', password='admin')
    user1.is_verified = True
    user1.save()

    fake = Faker()

    person = PtBrPersonProvider(fake)
    python = FakerPythonProvider(fake)

    categories = ['Meal', 'Breakfast', 'Soft Drink', 'Dessert', 'Others']

    for name in categories:
        Category.objects.create(name=name)

    for v in range(1000):
        # categories = Category.objects.all().order_by('?')
        # category = categories.first()

        Item.objects.create(
            name=person.name(),
            description='Coca‑Cola Original Taste is the world’s favourite soft drink and has been enjoyed since 1886.',
            price=python.pydecimal(right_digits=3, left_digits=2, positive=True),
            observation='',
            image='items/sushi_1.png',
            category_id=random.randint(1, 5)
        )


if __name__ == '__main__':
    init_db()
