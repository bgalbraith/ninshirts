from django.shortcuts import render_to_response
from catalog.models import Collection

def index(request):
    collections = Collection.objects.all()
    return render_to_response('catalog/index.html', {'collections': collections})

def collection(request, collection):
    _collection = Collection.objects.get(tag=collection)
    return render_to_response('catalog/collection.html', {'collection': _collection})