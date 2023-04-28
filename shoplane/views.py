from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .data import productes

# Create your views here.

class Productlist(View):
    def get(self, request):
        return JsonResponse(productes, safe=False)
