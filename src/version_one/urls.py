from django.urls import path, include
from version_one.auth import urls as auth_urls


urlpatterns = [
    path('auth/', include(auth_urls)),
]
