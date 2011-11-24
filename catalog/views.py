from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Collection

def index(request):
    collections = Collection.objects.all()
    return render_to_response('catalog/index.html', {'collections': collections})

def collection(request, collection):
    _collection = get_object_or_404(Collection.objects.all(), tag=collection)
    return render_to_response('catalog/collection.html', {'collection': _collection})