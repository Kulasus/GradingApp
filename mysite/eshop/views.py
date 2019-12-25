'''imports'''
from django.http import HttpResponse
from django.template import loader
from .models import Product


def index(request):
    '''home page view(index.html)'''
    newest_products_list = Product.objects.order_by('-created_at')[:10]
    template = loader.get_template('eshop/index.html')
    context = {'newest_products_list' : newest_products_list}
    return HttpResponse(template.render(context, request))

def categories(request):
    '''All categories view'''
    return HttpResponse("You are looking at all categories")

def category_detail(request, category_id):
    '''One exact category view'''
    response = "You are looking at category %s."
    return HttpResponse(response % category_id)

def products(request):
    '''All products view'''
    return HttpResponse("You are looking at all products")

def product_detail(request, product_id):
    '''One exact product view'''
    response = "You are looking at product %s."
    return HttpResponse(response % product_id)

def reviews(request):
    '''All newest reviews view'''
    return HttpResponse("You are looking at all reviews")
    