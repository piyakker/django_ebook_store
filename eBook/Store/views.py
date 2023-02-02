from django.shortcuts import render
from django.shortcuts import HttpResponse

def store_view(request):
    return HttpResponse("<h1>This is the Store</h1>")

def product_1_view(request):
    return HttpResponse('<h1>This is the Product1</h1>')