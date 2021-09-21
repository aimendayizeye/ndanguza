
from django.views import generic
from django.contrib.auth.models import User
from rest_framework.utils import serializer_helpers
from NdanguzaApi.models import *
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import permissions
class ListCategory(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# class ListBook(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated)
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# class DetailBook(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated) 
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListAdverts(generics.ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
class DetailAdverts(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated) 
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated) 
    queryset = User.objects.all()
    serializer_class= UserSerializer
class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated) 
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class ListCart(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
      queryset = Cart.objects.all()
      serializer_class = CartSerializer
