# Just for explanation, this middleware is not implemented.
from django.utils import translation


def language_middleware(get_response):
    def middleware(request):
        user = getattr(request, 'user', None)
        if user is not None and user.is_authenticated:
            translation.activate(user.interface_language)
        response = get_response(request)
        translation.deactivate()
        return response

    return middleware
