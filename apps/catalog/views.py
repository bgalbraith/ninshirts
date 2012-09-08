from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from apps.catalog.models import Category, Product

def index(request):
    categories = Category.objects.all()
    return render_to_response('catalog/index.html', {'categories': categories})

def category(request, category_tag):
    category = get_object_or_404(Category.objects.all(), tag=category_tag)
    return render_to_response('catalog/category.html', {'category': category})

def product(request, category_tag, product_tag):
    category = get_object_or_404(Category.objects.all(), tag=category_tag)
    product = get_object_or_404(Product.objects.all(), tag=product_tag)
    if category in product.deep_categories():
        return render_to_response('catalog/product.html', {'product': product})
    else:
        raise Http404
