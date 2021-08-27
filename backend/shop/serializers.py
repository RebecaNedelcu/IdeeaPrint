from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Illustration, Product, ProductDetails, ProductImages

# Serializers define the API representation.


class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustration
        fields = ['image', 'name']
        
    def get_image(self, illustration):
        request = self.context.get('request')
        image = illustration.image.url
        return request.build_absolute_uri(image)


class ProductSerializer(serializers.ModelSerializer):
    illustration = IllustrationSerializer()

    class Meta:
        model = Product
        fields = ['type', 'illustration']


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']


class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    product_images = ProductImagesSerializer(many=True)

    class Meta:
        model = ProductDetails
        fields = ['id', 'product', 'price', 'color', 'size', 'sex', 'quantity', 'product_images']

