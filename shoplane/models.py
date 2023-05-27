from django.db import models

# Create your models here.

class Rating(models.Model):
    rate=models.DecimalField(max_digits=3, decimal_places=2)
    count= models.IntegerField()

class Product(models.Model):
    product_id= models.IntegerField(default="")
    title= models.CharField(max_length=100)
    description= models.TextField(max_length=100,blank=True)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    image= models.ImageField()
    category= models.CharField(max_length=100)
    rating= models.ForeignKey(Rating, on_delete=models.CASCADE)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)
    status = models.TextField(max_length=100)
    sub_total = models.DecimalField(max_digits=25, decimal_places=2) 

class ProductReview(models.Model):
    review_id=models.IntegerField()
    product_id=models.IntegerField(default="")
    user_id=models.IntegerField()
    comment=models.CharField(max_length=1000)
    rating= models.DecimalField(max_digits=4, decimal_places=2)

class MyCartView(models.Model):
    cart_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    quantity = models.IntegerField()

class User(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    email_id=models.CharField(max_length=250, unique=True)
    password=models.CharField(max_length=100)