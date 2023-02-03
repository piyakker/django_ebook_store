from django.shortcuts import render, HttpResponseRedirect
from .models import Ebook, CartItem
from django.views.decorators.csrf import csrf_exempt

def store_view(request):
    ebooks = {'eBooks': Ebook.objects.all()}
    return render(request, 'Store/index.html', ebooks)

def cart_view(request):
    cart_item = CartItem.objects.all()
    cart_total = 0
    for item in cart_item:
        cart_total += item.price
    return render(request, 'Store/cart.html', {
        'cart_items': cart_item,
        'cart_total': cart_total
    })

@ csrf_exempt
def add_cart_item(request):
    book_id = request.POST['book_id']
    title = Ebook.objects.get(pk=book_id).title
    price = Ebook.objects.get(pk=book_id).price
    item = CartItem.objects.create(title = title, price = price)
    return HttpResponseRedirect('/store')