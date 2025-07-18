from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.

@api_view(['GET'])
def store(request):
    all_products = Product.objects.all()
    serialized_products = ProductSerializer(all_products, many = True)
    print(serialized_products)
    return Response(serialized_products.data)

@api_view(['POST'])
def create_product(request):
    return Response({'Action': 'Create new product'})