from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.views import View


class LoginIndex(View):
    
    def get(self, request):
        return HttpResponse('get')
    
    def post(self, request):
        return HttpResponse('post')