from .views import FavoriteViewset, ProductDetailsViewset, ProductViewset, illustrations_by_product_type, product_illustration_details, send_contact_message
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products/details', ProductDetailsViewset)
router.register('products', ProductViewset)
router.register('favorite', FavoriteViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('illustrations/<product_type>/', illustrations_by_product_type),
    path('productillustrationdetails/<product_type>/<illustration_id>/', product_illustration_details),
    # path('illustrations_all/', illustrations_all),
    path('sendcontactmessage/', send_contact_message),
]
