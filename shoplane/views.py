from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from .data import productes, cartitems
from .serializers import ProductSerializer, ProductReviewSerializer, MyCartViewSerializer, UserSerializer
import json

product_reviews=[]
cart_items=[]
users=[]

class Productlist(View):
    def get(self, request):
        return JsonResponse(productes, safe=False)

class Productdetails(View):
    def get(self,request,product_id):
        product=next((product for product in productes if product['product_id']== product_id), None)
        return JsonResponse(product,safe=False)

class ProductReview(View):

    def post(self, request, product_id):
        
        review_data=json.loads(request.body)
        review_data["product_id"]=product_id
        review_data["review_id"]=len(product_reviews)+1
        print(review_data)

        review_serialized=ProductReviewSerializer(data=review_data)
        if(review_serialized.is_valid()):
            product_reviews.append(review_serialized.data)

            return JsonResponse(review_serialized.data, safe=False)
        else:
            return JsonResponse(review_serialized.errors, safe=False)

class MyCartView(View):
    def get(self, request, cart_id):
        cart=next((cart for cart in cartitems if cart['cart_id']== cart_id), None)
        return JsonResponse(cart,safe=False)

class CartView(View):
    def post(self, request, cart_id):
        
        cart_data=json.loads(request.body)
        cart_data["cart_id"]=cart_id
        cart_data["cart_id"]=len(cart_items)+1
        print(cart_data)

        cart_serialized=MyCartViewSerializer(data=cart_data)
        if(cart_serialized.is_valid()):
            cart_items.append(cart_serialized.data)

            return JsonResponse(cart_serialized.data, safe=False)
        else:
            return JsonResponse(cart_serialized.errors, safe=False)

class UpdateCart(View):
    def put(self, request, cart_id):
        cart_data=json.loads(request.body)
        cart_serialized=MyCartViewSerializer(data=cart_data)
        if(cart_serialized.is_valid()):
            cart_to_update=None
            for index, item in enumerate(cart_items):
                if(item["cart_id"]==cart_id):
                    cart_to_update=item
                    break
            if(cart_to_update):
                cart_items[index]=cart_serialized.data
                return JsonResponse(cart_serialized.data, safe=False)
            return JsonResponse(cart_serialized.errors, safe=False)

class CheckoutView(View):
    def delete(self, request, cart_id):
        for index, item in enumerate(cart_items):
            if(item["cart_id"]==cart_id):
                cart_items.remove(item)
                return JsonResponse("Item is deleted",safe=False)
        return HttpResponseBadRequest({"Something went wrong"})

class SearchView(View):
    def get(self,request):
        find = []
        query = request.GET.get("query")
        for val in productes:
            if query in val["title"]:
                find.append(val)
        find_serialized = ProductSerializer(find, many=True).data
        return JsonResponse(find_serialized, safe=False)

class UserSignup(View):
    def post(self, request):
        user_data=json.loads(request.body)
        user_data["user_id"]=len(users)+1
        user_serialized=UserSerializer(data=user_data)
        if(user_serialized.is_valid()):
            users.append(user_serialized.data)
            return JsonResponse("Registered successfully", safe=False)
        else:
            return JsonResponse(user_serialized.errors, safe=False)

class UserSignin(View):
    def post(self, request):
        user_data=json.loads(request.body)
        print(user_data)
        print(user_data["email_id"])
        for index, item in enumerate(users):
                if(item["email_id"]==user_data["email_id"] and item["password"]==user_data["password"]):
                    return JsonResponse("Login is Successful", safe=False)
        return JsonResponse("Login is not Successful", safe=False)
    