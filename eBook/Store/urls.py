from django.urls import path
from .views import *

urlpatterns = [
    path('', store_view),
    path('p1', product_1_view)
]