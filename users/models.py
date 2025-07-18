from django.db import models

# Create your models here.

class Seller(models.Model):
    seller_name = models.CharField(max_length=100)

    def __str__(self):
        return self.seller_name