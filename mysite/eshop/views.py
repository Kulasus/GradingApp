from django.http import HttpResponse
from django.template import loader
from .models import Product


def index(request):
    newest_products_list = Product.objects.order_by('-created_at')[:10]
    template = loader.get_template('eshop/index.html')
    context = {'newest_products_list' : newest_products_list}
    
    return HttpResponse(template.render(context,request))
    
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
    