from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.routers import Response

from .models import ContactMessage, Illustration, Product, ProductDetails
from .serializers import (ContactMessageSerializer, IllustrationSerializer, ProductDetailsSerializer,
                          ProductSerializer)


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailsViewset(viewsets.ModelViewSet):
    serializer_class = ProductDetailsSerializer
    queryset = ProductDetails.objects.all()


class ContactMessageViewset(viewsets.ModelViewSet):
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()


@api_view(('GET',))
@permission_classes([])
def illustrations_by_product_type(request, product_type: int):
    illustrations =  Illustration.objects.filter(products__type=product_type)
    serialized_illustrations = IllustrationSerializer(illustrations, many=True, context={"request": request})
    
    response = Response(data=serialized_illustrations.data)
    
    return response


@api_view(['POST'])
@permission_classes([])
def send_contact_message(request):
    response = Response(status_code=400)
    contactMessage = ContactMessage()
    serializer = ContactMessageSerializer(contactMessage, data = request.data)
    if (serializer.is_valid()):
        serializer.save()
        response.status_code = 200
    return response

