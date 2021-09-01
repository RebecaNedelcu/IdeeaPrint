from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import ContactMessage, Favorite, Illustration, Order, OrderProducts, Product, ProductDetails, ProductIllustration, ProductImages
from accounts.serializers import UserSerializer
# Serializers define the API representation.


class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustration
        fields = ['id', 'image', 'name', 'created_at', 'price']

    def get_image(self, illustration):
        request = self.context.get('request')
        image = illustration.image.url
        return request.build_absolute_uri(image)


class ProductSerializer(serializers.ModelSerializer):
    #illustration = IllustrationSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'type', 'price', 'color']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']


class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductDetails
        fields = ['id', 'product',  'size',
                  'sex', 'quantity']


class ProductIllustrationSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    illustration = IllustrationSerializer()

    class Meta:
        model = ProductIllustration
        fields = ['id', 'product', 'illustration', 'image']


class FavoriteSerializer(serializers.ModelSerializer):
    illustration = IllustrationSerializer()
    user = UserSerializer()

    class Meta:
        model = Favorite
        fields = ['id', 'illustration', 'user']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'company',
            'street',
            'city',
            'zipcode',
            'county',
            'country',
            'payment_type',
            'status',
            'delivery_date',
        ]


class OrderedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = [
            'order',
            'product',
            'quantity',
            'price',
            'illustration',
            'illustration_from_user',
        ]
