from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Welcome to ebook store</h1>
    <img src="https://i.ibb.co/Y7Yq32N/all-bk-set.png">
    """)