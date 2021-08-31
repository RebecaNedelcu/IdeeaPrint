from .views import FavoriteViewset, ProductDetailsViewset, ProductViewset, illustrations_by_product_type, send_contact_message
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products/details', ProductDetailsViewset)
router.register('products', ProductViewset)
router.register('favorite', FavoriteViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('illustrations/<product_type>/', illustrations_by_product_type),
    path('sendcontactmessage/', send_contact_message)
]
