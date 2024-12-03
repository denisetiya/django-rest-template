
from django.http import JsonResponse


def not_found(request, exception=None):
    return JsonResponse({"detail": "The requested resource was not found."}, status=404)
