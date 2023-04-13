from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import View
# Create your views here.
class Categories(View):
    def ju(request):
        categories=Categories.objects.all()
        return {'categories':categories}

def categories(request):
    return{
        'categories':Category.objects.all()
    }
class Allproducts(View):
    def get(self, request):
        products=Product.objects.all()
        context = {
            'products':products,
        }
        return render(request, 'store/home.html', context) 
    
class Productdetail(View):
    def get(self, request, slug):
        product=get_object_or_404(Product, slug=slug, inStock=True)
        return render(request, 'store/products/detail.html', {'product':product})
    

class Categorylist(View):
    def get(self, request, cslug):
        category=get_object_or_404(Category, slug=cslug)
        products=Product.objects.filter(category=category)
        context={'category': category, 'products':products}
        return render(request, 'store/products/category.html', context)











# def categories(request):
#     return {
#         'categories': Category.objects.all()
#     }


# def all_products(request):
#     products = Product.objects.all()
#     return render(request, 'store/home.html', {'products': products})


# def category_list(request, category_slug=None):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)
#     return render(request, 'store/products/category.html', {'category': category, 'products': products})


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, in_stock=True)
#     return render(request, 'store/products/detail.html', {'product': product})