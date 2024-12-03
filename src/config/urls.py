
from django.contrib import admin
from django.urls import path, include
from version_one import urls
from .exception_handler import not_found

handler404 = not_found

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/v1/', include(urls)),
]
