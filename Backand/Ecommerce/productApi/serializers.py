from rest_framework import serializers
from .models import Product # type: ignore

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'discount', 'categories']  # Only the required fields
