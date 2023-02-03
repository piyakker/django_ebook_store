from django.urls import path
from .views import *

urlpatterns = [
    path('', store_view),
    path('cart', cart_view),
    path('cart_add_item/', add_cart_item),
    path('cart/del_cart_item/', del_cart_item)
]