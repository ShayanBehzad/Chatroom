from urllib.parse import urlencode
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, HttpResponseRedirect




class UrlModifierMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        query_params = request.GET.copy()
        if not request.path_info.startswith('/chatroom'):
            request.path_info = '/chatroom' + request.path_info

        response = self.get_response(request)

        return response
