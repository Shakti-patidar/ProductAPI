from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import ProductSerializer # type: ignore
from rest_framework.response import Response
from rest_framework import status
from .models import Product

@api_view(['POST' , 'GET'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the created product data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails
    if request.method == 'GET':
        # If you want to return a list of products on GET
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['DELETE','PUT'])    
def modify_product(request, pk):
    try:
        
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Create your views here.
def add_product_page(request):
                return render(request, 'productApi/add_product_page.html')
    
def product_list_page(request):
    return render(request, 'productApi/product_list.html')     

def editing_product_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'productApi/editing_product.html', {'product': product})