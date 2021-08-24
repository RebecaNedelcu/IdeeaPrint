from django.contrib import admin
from .models import Illustration, Product, ProductDetails, ProductImages


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