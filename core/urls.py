from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.routes.api_v1_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


