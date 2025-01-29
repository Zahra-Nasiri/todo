from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST


class ValidationErrorMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, DjangoValidationError):
            error_message = exception.message_dict if hasattr(
                exception, 'message_dict') else list(exception.messages)
            return JsonResponse(
                {'error': error_message},
                status=HTTP_400_BAD_REQUEST,
            )

        if isinstance(exception, DRFValidationError):
            return JsonResponse(
                {'error': exception.detail},
                status=HTTP_400_BAD_REQUEST,
            )

        return None
