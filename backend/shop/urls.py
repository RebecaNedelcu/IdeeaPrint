from .views import ProductDetailsViewset, ProductViewset, illustrations_by_product_type
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products/details', ProductDetailsViewset)
router.register('products', ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('illustrations/<product_type>/', illustrations_by_product_type),
]
