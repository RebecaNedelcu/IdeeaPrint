from django.contrib import admin
from .models import ContactMessage, Illustration, Order, OrderProducts, Product, ProductDetails, ProductImages


class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailsInline]


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Illustration)
class IllustrationAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    pass