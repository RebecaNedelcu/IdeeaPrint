from django.shortcuts import render
from rest_framework import viewsets

from .models import Product, ProductDetails
from .serializers import ProductDetailsSerializer, ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailsViewset(viewsets.ModelViewSet):
    serializer_class = ProductDetailsSerializer
    queryset = ProductDetails.objects.all()

    
