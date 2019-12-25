from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the eshop index.")

def categories(request):
    return HttpResponse("You are looking at all categories")

def category_detail(request, category_id):
    response = "You are looking at category %s."
    return HttpResponse(response % category_id)

def products(request):
    return HttpResponse("You are looking at all products")

def product_detail(request, product_id):
    response = "You are looking at product %s."
    return HttpResponse(response % product_id)

def reviews(request):
    return HttpResponse("You are looking at all reviews")
    