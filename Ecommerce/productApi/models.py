from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    categories = models.CharField(max_length=100)
    
    
    def discounted_price(self):
        return self.price - (self.price * (self.discount / 100))
    def __str__(self):
        return self.name
# Create your models here.
