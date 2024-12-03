from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed



def Res(status, message, error=None, content=None):
    res = {
        'status': status,
        'message': message,
    }
    if error is not None:
        res['error'] = error
    if content is not None:
        res['content'] = content
    return Response(res, status=status)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    
    



# Custom Token Obtain View (for login)
class TokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            # Customize the successful response
            return Res(status.HTTP_200_OK, 'Token obtained successfully', None, response.data)
        except AuthenticationFailed as e:
            # Handle authentication failure
            return Res(status.HTTP_401_UNAUTHORIZED, 'Authentication failed', str(e), None)
        except TokenError as e:
            # Handle token errors
            return Res(status.HTTP_400_BAD_REQUEST, 'Token error', str(e), None)
        except Exception as e:
            # Catch all other exceptions
            return Res(status.HTTP_400_BAD_REQUEST, 'An unexpected error occurred', str(e), None)

# Custom Token Refresh View
class TokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Res(status.HTTP_200_OK, 'Token refreshed successfully', None, response.data)
        except InvalidToken as e:
            # Handle invalid token errors (e.g., expired token)
            return Res(status.HTTP_401_UNAUTHORIZED, 'Invalid token', str(e), None)
        except TokenError as e:
            return Res(status.HTTP_400_BAD_REQUEST, 'Token error', str(e), None)
        except Exception as e:
            return Res(status.HTTP_400_BAD_REQUEST, 'An unexpected error occurred', str(e), None)

# Custom Token Verify View
class TokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            return Res(status.HTTP_200_OK, 'Token verified successfully', None, response.data)
        except InvalidToken as e:
            return Res(status.HTTP_401_UNAUTHORIZED, 'Invalid token', str(e), None)
        except TokenError as e:
            return Res(status.HTTP_400_BAD_REQUEST, 'Token error', str(e), None)
        except Exception as e:
            return Res(status.HTTP_400_BAD_REQUEST, 'An unexpected error occurred', str(e), None)

