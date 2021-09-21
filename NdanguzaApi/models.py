from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Location(models.Model):
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.location
class Product(models.Model):
    productName = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',related_name='products',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_created=True)
    imageUrl = models.URLField()
    location = models.ForeignKey(Location,related_name='product_location',on_delete=CASCADE)
    class Meta:
        ordering = ['-date_created'] 
    def __str__(self) :
        return self.productName
# class Book(models.Model):
#     title = models.CharField(max_length=50)
#     price = models.IntegerField()
#     pages = models.IntegerField()
#     isbn = models.CharField(max_length=13)
#     description = models.TextField()
#     category = models.ForeignKey(Category,related_name="books",on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_created=True)
#     imageUrl = models.URLField()

#     class Meta:
#         ordering =['-date_created'] 
#     def __str__(self) :
#         return self.title

class Advert(models.Model):
    product = models.ForeignKey(Product,related_name='product_advert',on_delete=CASCADE)
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title
class Cart(models.Model):
    product = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True)
    cart_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    class Meta:
        ordering = ["cart_id","-date_created"]

    def __str__(self):
        return f'{self.cart_id}'