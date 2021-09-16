from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='onecat'),
    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>/',DetailBook.as_view(),name='onebook'),
    path('products',ListProduct.as_view(),name='products'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='oneproduct'),
    path('adverts',ListAdverts.as_view(),name='adverts'),
    path('adverts/<int:pk>/',DetailAdverts.as_view(),name='oneadv'),
    path('advertise/<int:pk>/',views.advertise,name='adv'),
    path('allproducts',views.productList,name='fromdef')
]