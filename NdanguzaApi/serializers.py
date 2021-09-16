

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
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book
class AdvertSerializer(serializers.ModelSerializer):
     class Meta:
        fields = (
            'title',
            'product'
        )
        model = Advert

