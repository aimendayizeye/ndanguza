
from django.views import generic
from rest_framework.utils import serializer_helpers
from NdanguzaApi.models import *
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListAdverts(generics.ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
class DetailAdverts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

@api_view(['GET',])
def productList(request):
    if request.method=='GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    else:
        return Response(serializers.Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# def advertise(request,pk,*args, **kwargs):
#     if request.method == 'GET':
#         product = Product.objects.get(pk=pk)
#         adverts = Advert.objects.add(product)
#         serializer= Advert(adverts,many=False)
#         print(serializer.data)
#         return Response(serializer.data)
#     else:
#         return Response(serializers.Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       