from accounts.serializers import UserSerializer
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.routers import Response

from .models import ContactMessage, Illustration, Order, OrderProducts, Product, ProductDetails, Favorite, ProductIllustration
from .serializers import (ContactMessageSerializer, FavoriteSerializer, IllustrationSerializer, OrderSerializer, OrderedProductsSerializer, ProductDetailsSerializer, ProductIllustrationSerializer,
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
@authentication_classes([])
def illustrations_by_product_type(request, product_type: int):
    illustrations = Illustration.objects.filter(
        products_type__type=product_type)
    serialized_illustrations = IllustrationSerializer(
        illustrations, many=True, context={"request": request})

    response = Response(data=serialized_illustrations.data)

    return response


@api_view(('GET',))
@permission_classes([])
@authentication_classes([])
def product_illustration_details(request, product_type: int, illustration_id: int):
    if product_type == 0:
        products_illustrations = ProductIllustration.objects.filter(
            illustration=illustration_id)
    else:
        products_illustrations = ProductIllustration.objects.filter(
            product__type=product_type, illustration=illustration_id)
    serialized_illustrations = ProductIllustrationSerializer(
        products_illustrations, many=True, context={"request": request})

    response = Response(data=serialized_illustrations.data)

    return response


@api_view(['POST'])
@permission_classes([])
def send_contact_message(request):
    response = Response()
    contactMessage = ContactMessage()
    serializer = ContactMessageSerializer(contactMessage, data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        response.status = 200
    else:
        response.status = 400
    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorite(request):
    favorite = Favorite.objects.filter(user=request.user)
    serialized_data = FavoriteSerializer(
        favorite, many=True, context={'request': request})

    return Response(serialized_data.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request, illustration_id):
    favorite = Favorite.objects.filter(
        user=request.user, illustration=illustration_id).first()
    if favorite is not None:
        favorite.delete()
    else:
        Favorite.objects.create(
            user=request.user, illustration=Illustration.objects.get(id=illustration_id))

    return Response()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_product_details(request, product_id):
    product_details = ProductDetails.objects.filter(product=product_id)
    serialized_data = ProductDetailsSerializer(product_details, many=True)

    return Response(serialized_data.data)


@api_view(['GET'])
@permission_classes([])
def get_products_by_type(request, product_type):
    product = Product.objects.filter(type=product_type)
    serialized_data = ProductSerializer(
        product, many=True, context={'request': request})

    return Response(serialized_data.data)


class OrderViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderProductViewset(viewsets.ModelViewSet):
    serializer_class = OrderedProductsSerializer
    queryset = OrderProducts.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = []


@api_view(['GET'])
@permission_classes([])
def get_product_details_for_cart(request, product_id, size):
    product_details = ProductDetails.objects.get(
        product__id=product_id, size=size)
    serialized_data = ProductDetailsSerializer(product_details)

    return Response(serialized_data.data)
