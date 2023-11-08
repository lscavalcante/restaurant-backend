from rest_framework import routers
from django.urls import path, include

from apps.authentication.views import AuthenticationAPI
from apps.category.views import CategoryAPI
from apps.item.views import ItemAPI
from apps.user.views import UserAPI
from apps.order.views import OrderAPI

router = routers.DefaultRouter()
router.register(r"authentication", AuthenticationAPI, basename='authentication')
router.register(r"users", UserAPI)
router.register(r"items", ItemAPI)
router.register(r"categories", CategoryAPI)
router.register(r"orders", OrderAPI)

urlpatterns = [
    path("", include(router.urls)),
]
