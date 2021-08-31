from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth.models import User

from .constants import PAYMENT_TYPES, PRODUCT_SEX_TYPE, PRODUCT_SIZES, PRODUCT_TYPES, STATUS_TYPES


class Illustration(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Illustration - {self.name}"




class Product(models.Model):
    name = models.CharField(max_length=125)
    type = models.CharField(choices=PRODUCT_TYPES, max_length=4)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    color = ColorField(default='#000000')

    def __str__(self):
        return f"{self.name} - Color {self.color} "


class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(choices=PRODUCT_SIZES, max_length=6)
    sex = models.CharField(choices=PRODUCT_SEX_TYPE, max_length=6)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product} - Size {self.get_size_display()}  - Sex {self.sex}"

    class Meta:
        verbose_name = 'Product Details'
        verbose_name_plural = 'Product Details'


class ProductIllustration(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    illustration = models.ForeignKey(Illustration, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.product} - {self.illustration} - image"


    class Meta:
        unique_together = [('product',  'illustration')]
        verbose_name = 'Product Illustration'
        verbose_name_plural = 'Products Illustrations'  


class IllustrationProductType(models.Model):
    illustration = models.ForeignKey(Illustration, on_delete=models.CASCADE, related_name='products_type')
    type = models.CharField(max_length=10, choices=PRODUCT_TYPES)

    def __str__(self):
        return f"{self.illustration} - {self.get_type_display()}"


@DeprecationWarning
class ProductImages(models.Model):
    product_details = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField()

    def __str__(self):
        return f"{self.product} - image"

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Favorite(models.Model):
    illustration = models.ForeignKey(Illustration, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user} - {self.illustration}"

    class Meta:
        unique_together = [('user',  'illustration')]


class Order(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    county = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_TYPES)
    delivery_date = models.DateField()

    def __str__(self):
        return f"Order #{self.id} for {self.first_name} {self.last_name}"


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product} in {self.order}"

    def clean(self):
        previous_quantity = 0
        if self.id is not None:
            previous_quantity = self.__class__.objects.get(pk=self.id).quantity
        if self.quantity > previous_quantity + self.product.quantity:
            raise ValidationError('Stock too low')

    def save(self, *args, **kwargs):
        previous_quantity = 0
        if self.id is not None:
            previous_quantity = self.__class__.objects.get(pk=self.id).quantity
        self.product.quantity = self.product.quantity - self.quantity + previous_quantity
        self.product.save()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('order', 'product')
        verbose_name = 'Order Product'
        verbose_name_plural = 'Orders Products'


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"Message from {self.name}, {self.email} : {self.message}"
