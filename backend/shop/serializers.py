from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import ContactMessage, Favorite, Illustration, Product, ProductDetails, ProductIllustration, ProductImages
from accounts.serializers import UserSerializer
# Serializers define the API representation.


class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustration
        fields = ['id','image', 'name', 'created_at']
        
    def get_image(self, illustration):
        request = self.context.get('request')
        image = illustration.image.url
        return request.build_absolute_uri(image)


class ProductSerializer(serializers.ModelSerializer):
    #illustration = IllustrationSerializer()

    class Meta:
        model = Product
        fields = ['id','name','type','price','color']


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


class ProductIllustrationSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    illustration = IllustrationSerializer()

    class Meta:
        model = ProductIllustration
        fields = ['id','product','illustration','image']

class FavoriteSerializer(serializers.ModelSerializer):
    illustration = IllustrationSerializer()
    user = UserSerializer()

    class Meta:
        model = Favorite
        fields = ['id','illustration','user']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id','name','email','message']
