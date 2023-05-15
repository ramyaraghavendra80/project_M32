from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .data import productes

# Create your views here.

class Productlist(View):
    def get(self, request):
        return JsonResponse(productes, safe=False)

class Productdetails(View):
    def get(self,request,product_id):
        product=next((product for product in productes if product['product_id']== product_id), None)
        return JsonResponse(product,safe=False)
        