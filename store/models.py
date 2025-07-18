from django.db import models
from users.models import Seller
# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_description = models.TextField()
    initial_price = models.PositiveIntegerField(null=True, blank=True)
    current_price = models.PositiveIntegerField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to='product_images/')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=1)
    is_dicounted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)

#JSON - Javascript Object Notation 

    def __str__(self):
        return self.product_name