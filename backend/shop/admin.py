from .models import ContactMessage, Favorite, Illustration, IllustrationProductType, Order, OrderProducts, Product, ProductDetails, ProductIllustration, ProductImages
from django.contrib import admin


class ProductDetailsInline(admin.TabularInline):
    model = ProductDetails


class IllustrationProductTypeInline(admin.TabularInline):
    model = IllustrationProductType
    max_num = 4


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailsInline]

# @DeprecationWarning
# @admin.register(ProductImages)
# class ProductImagesAdmin(admin.ModelAdmin):
#     pass


@admin.register(Illustration)
class IllustrationAdmin(admin.ModelAdmin):
    pass
    inlines = [IllustrationProductTypeInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductIllustration)
class ProductIllustrationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
