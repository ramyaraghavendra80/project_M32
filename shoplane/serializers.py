from rest_framework import serializers
from .models import Product, Rating, Order, ProductReview, MyCartView,User


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    rating=RatingSerializer()
    class Meta:
        model=Product
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model=Order
        fields='__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductReview
        fields='__all__'

class MyCartViewSerializer(serializers.ModelSerializer):
    class Meta:
        model= MyCartView
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'