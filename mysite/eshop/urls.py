from django.urls import path
from . import views

urlpatterns = [
    #mainviews
    path('', views.index, name='index'),
    path('categories/', views.categories, name="categories"),
    path('products/', views.products, name="products"),
    path('reviews/', views.reviews, name="review"),
    #subviews
    path('categories/<int:category_id>', views.category_detail, name="category_detail"),
    path('products/<int:product_id>', views.product_detail, name="product_detail")
]