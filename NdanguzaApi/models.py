from django.db import models
from django.db.models.deletion import CASCADE

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
    date_created = models.DateTimeField(auto_created=True)
    imageUrl = models.URLField()
    location = models.ForeignKey(Location,related_name='product_location',on_delete=CASCADE)
    class Meta:
        ordering = ['-date_created'] 
    def __str__(self) :
        return self.productName
class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    pages = models.IntegerField()
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    category = models.ForeignKey(Category,related_name="books",on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_created=True)
    imageUrl = models.URLField()

    class Meta:
        ordering =['-date_created'] 
    def __str__(self) :
        return self.title

class Advert(models.Model):
    product = models.ForeignKey(Product,related_name='product_advert',on_delete=CASCADE)
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title

