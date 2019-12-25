'''some import'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    '''Category module for db'''
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Name: " + self.name

class Product(models.Model):
    '''Product module for db'''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return "Name: " + self.name

class Review(models.Model):
    '''Review module for db'''
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
