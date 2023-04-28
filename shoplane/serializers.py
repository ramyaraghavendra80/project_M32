from rest_framework import serializers
from .models import Product
from .models import Rating


class ProductSerializer(serializers.ModelSerializer):
    rating=RatingSerializer()
    class Meta:
        model=Products
        fields='__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model=Order
        fields='__all__'