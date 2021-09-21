

from re import T
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = Category
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = Product
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#         model = Book
class AdvertSerializer(serializers.ModelSerializer):
     class Meta:
        fields = (
            'title',
            'product'
        )
        model = Advert

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True,queryset = Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'products'
        )

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True,many=True)
    class Meta:
        model = Cart
        fields = '__all__'