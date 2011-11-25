from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Collection, Shirt

def index(request):
    collections = Collection.objects.all()
    return render_to_response('catalog/index.html', {'collections': collections})

def collection(request, collection_tag):
    collection = get_object_or_404(Collection.objects.all(), tag=collection_tag)
    return render_to_response('catalog/collection.html', {'collection': collection})

def shirt(request, shirt_tag):
    shirt = get_object_or_404(Shirt.objects.all(), tag=shirt_tag)
    return render_to_response('catalog/shirt.html', {'shirt': shirt})