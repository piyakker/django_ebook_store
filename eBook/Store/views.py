from django.shortcuts import render
from .models import Ebook

def store_view(request):
    ebooks = {'eBooks': Ebook.objects.all()}
    return render(request, 'Store/index.html', ebooks)

def cart_view(request):
    return render(request, 'Store/cart.html')