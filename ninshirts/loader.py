import os
import sys
import site
import zipfile

if len(sys.argv) == 1:
    print "Usage: loader.py archive"
    sys.exit(0)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
    sys.path.append(PROJECT_DIR)

# assumes that the entire project is inside the virtualenv directory
site.addsitedir(BASE_DIR + '/../lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ninshirts.settings")


from django.core.files.base import ContentFile
from apps.catalog.models import Product, Option

zf = zipfile.ZipFile(sys.argv[1])
products = {}
for file in sorted(zf.namelist()):
    name, color, order, ext = file.split('.')
    if name not in products:
        products[name] = {'color': color, 'images': [file]}
    else:
        products[name]['images'].append(file)

for k,v in products.items():
    product = Product(name=k, tag=k)
    product.save()
    color = Option.objects.get(abbreviation=v['color'])
    product.options.add(color)
    product.save()
    for file in v['images']:
        img = product.productimage_set.create()
        content = ContentFile(zf.read(file))
        img.original.save(file, content)
    product.save()

zf.close()