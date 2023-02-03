from django.urls import path
from .views import *

urlpatterns = [
    path('', store_view),
    path('cart', cart_view)
]