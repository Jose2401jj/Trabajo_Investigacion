from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = resolve(request.path_info).url_name
        if not request.user.is_authenticated and current_url not in ['login', 'logout', 'register']:
            return redirect(settings.LOGIN_URL)
        
        return self.get_response(request)