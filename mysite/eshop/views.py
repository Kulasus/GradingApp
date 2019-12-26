'''imports'''
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Category, Review



def index(request):
    '''home page view(index.html)'''
    newest_products_list = Product.objects.order_by('-created_at')[:10]
    context = {'newest_products_list' : newest_products_list}
    return render(request, 'eshop/index.html', context)

def categories(request):
    '''All categories view'''
    all_categories_list = Category.objects.all()
    context = {'all_categories_list' : all_categories_list}
    return render(request, 'eshop/categories.html', context)

def category_detail(request, category_id):
    '''One exact category view'''
    response = "You are looking at category %s."
    return HttpResponse(response % category_id)

def products(request):
    '''All products view'''
    all_products_list = Product.objects.all()
    context = {'all_products_list' : all_products_list}
    return render(request, 'eshop/products.html', context)

def product_detail(request, product_id):
    '''One exact product view'''
    response = "You are looking at product %s."
    return HttpResponse(response % product_id)

def reviews(request):
    '''All newest reviews view'''
    all_reviews_list = Review.objects.order_by('-created_at')[:5]
    context = {'all_reviews_list' : all_reviews_list}
    return render(request, 'eshop/reviews.html', context)

    