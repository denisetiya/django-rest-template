
from django.urls import path, include

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .views import RegisterView, TokenObtainPairView, TokenRefreshView, TokenVerifyView
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_route(request):
    return JsonResponse({"message": "This is a protected route. success"})

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', RegisterView.as_view(), name='register'),
    path('protected', protected_route, name='protected_route'),
]