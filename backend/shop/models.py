from django.db import models
from django.db.models.aggregates import Max
from .constants import PRODUCT_SEX_TYPE, PRODUCT_SIZES, PRODUCT_TYPES
from colorfield.fields import ColorField

# Create your models here.
class Illustration(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Illustration - {self.name}"


class Product(models.Model):
    illustration = models.ForeignKey(Illustration, on_delete=models.CASCADE)
    type = models.CharField(choices=PRODUCT_TYPES, max_length=4)

    def __str__(self):
        return f"{self.illustration}"


class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    color = ColorField(default='#000000')
    size = models.CharField(choices=PRODUCT_SIZES, max_length=6)
    sex = models.CharField(choices=PRODUCT_SEX_TYPE, max_length=6)
    cantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product} - Size {self.get_size_display()} - Color {self.color} - Sex {self.sex}"

    class Meta:
        verbose_name = 'Product Details'
        verbose_name_plural = 'Product Details'


class ProductImages(models.Model):
    product_details = models.ForeignKey(
        ProductDetails, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField()

    def __str__(self):
        return f"{self.product_details} - image"

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
