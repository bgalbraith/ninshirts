from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from apps.catalog.models import Category, Product, ProductImage

def index(request):
    categories = Category.objects.all()
    return render_to_response('catalog/index.html',
        {'categories': categories}, context_instance=RequestContext(request))

def category(request, category_tag):
    category = get_object_or_404(Category.objects.all(), tag=category_tag)
    return render_to_response('catalog/category.html',
        {'category': category}, context_instance=RequestContext(request))

def product(request, category_tag, product_tag):
    category = get_object_or_404(Category.objects.all(), tag=category_tag)
    product = get_object_or_404(Product.objects.all(), tag=product_tag)
    if category in product.deep_categories():
        images = ProductImage.objects.filter(
            pk__in=product.get_productimage_order())
        # force caching of zoom spec if needed
        for image in images:
            url = image.zoom.url
        return render_to_response('catalog/product.html',
            {'product': product, 'images': images},
            context_instance=RequestContext(request))
    else:
        raise Http404