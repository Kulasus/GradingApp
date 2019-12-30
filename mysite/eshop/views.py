'''imports'''
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Review, User



def index(request):
    '''home page view(index.html)'''
    newest_products_list = Product.objects.order_by('-created_at')[:10]
    return render(request, 'eshop/index.html', {'newest_products_list' : newest_products_list})

def categories(request):
    '''All categories view'''
    all_categories_list = Category.objects.all()
    return render(request, 'eshop/categories.html', {'all_categories_list' : all_categories_list})

def category_detail(request, category_id):
    '''One exact category view'''
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'eshop/category_detail.html', {'category' : category})

def products(request):
    '''All products view'''
    all_products_list = Product.objects.all()
    return render(request, 'eshop/products.html', {'all_products_list' : all_products_list})

def product_detail(request, product_id):
    '''One exact product view'''
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'eshop/product_detail.html', {'product':product})

def reviews(request):
    '''All newest reviews view'''
    all_reviews_list = Review.objects.order_by('-created_at')[:5]
    return render(request, 'eshop/reviews.html', {'all_reviews_list' : all_reviews_list})

def user_profile(request, user_id):
    '''User profile view'''
    user = get_object_or_404(User, id=user_id)
    return render(request, 'eshop/user_profile.html', {'user':user})

def login(request):
    '''Login view'''
    return render(request, 'eshop/login')
    
def signup(request):
    '''Singup view'''
    return render(request, 'eshop/signup.html')
    