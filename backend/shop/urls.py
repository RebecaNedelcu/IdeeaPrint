from .views import FavoriteViewset, ProductDetailsViewset, ProductViewset, get_favorite, get_product_details, illustrations_by_product_type, product_illustration_details, send_contact_message, toggle_favorite
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products/details', ProductDetailsViewset)
router.register('products', ProductViewset)
router.register('favorite', FavoriteViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('illustrations/<product_type>/', illustrations_by_product_type),
    path('productillustrationdetails/<product_type>/<illustration_id>/',
         product_illustration_details),
    path('sendcontactmessage/', send_contact_message),
    path('get_favorite/', get_favorite),
    path('toggle_favorite/<illustration_id>', toggle_favorite),
    path('get_product_details/<product_id>', get_product_details),
]
