from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.routers import Response

from .models import ContactMessage, Illustration, Product, ProductDetails, Favorite, ProductIllustration
from .serializers import (ContactMessageSerializer, FavoriteSerializer, IllustrationSerializer, ProductDetailsSerializer, ProductIllustrationSerializer,
                          ProductSerializer)


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailsViewset(viewsets.ModelViewSet):
    serializer_class = ProductDetailsSerializer
    queryset = ProductDetails.objects.all()


class FavoriteViewset(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()


@api_view(('GET',))
@permission_classes([])
def illustrations_by_product_type(request, product_type: int):
    illustrations =  Illustration.objects.filter(products_type__type=product_type)
    serialized_illustrations = IllustrationSerializer(illustrations, many=True, context={"request": request})
    
    response = Response(data=serialized_illustrations.data)
    
    return response


# @api_view(('GET',))
# @permission_classes([])
# def illustrations_all(request):
#     illustrations =  Illustration.objects.prefetch_related('products_type').all()
#     serialized_illustrations = IllustrationSerializer(illustrations, many=True, context={"request": request})
    
#     response = Response(data=serialized_illustrations.data)
    
#     return response


@api_view(('GET',))
@permission_classes([])
def product_illustration_details(request, product_type: int,illustration_id: int):
    products_illustrations = ProductIllustration.objects.filter(product__type=product_type, illustration = illustration_id)
    serialized_illustrations = ProductIllustrationSerializer(products_illustrations, many=True, context={"request": request})
    
    response = Response(data=serialized_illustrations.data)
    
    return response



@api_view(['POST'])
@permission_classes([])
def send_contact_message(request):
    response = Response()
    contactMessage = ContactMessage()
    serializer = ContactMessageSerializer(contactMessage, data = request.data)
    if (serializer.is_valid()):
        serializer.save()
        response.status = 200
    else:
        response.status = 400
    return response

