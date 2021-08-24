from .views import ProductDetailsViewset, ProductViewset
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products/details', ProductDetailsViewset)
router.register('products', ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]
