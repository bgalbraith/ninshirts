from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Category

def index(request):
    categories = Category.objects.all()
    return render_to_response('catalog/index.html', {'categories': categories})

def category(request, category_tag):
    category = get_object_or_404(Category.objects.all(), tag=category_tag)
    return render_to_response('catalog/category.html', {'category': category})

def product(request, category_tag, product_tag):
    category = get_object_or_404(Category.objects.all(), tag=category_tag)
    product = get_object_or_404(category.product_set.all(), tag=product_tag)
    return render_to_response('catalog/product.html', {'product': product})