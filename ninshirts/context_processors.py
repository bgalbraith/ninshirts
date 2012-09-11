from apps.catalog.models import Category
import re

def sidenav(request):
    """Generate the appropriate sidebar navigation expansion."""
    active_category = None
    include = []
    m = re.search(r'^/([a-z0-9-]+)/', request.path)
    if m is not None:
        tag = m.group(1)
        try:
            active_category = Category.objects.get(tag__exact=tag)
        except Category.DoesNotExist:
            pass

    if active_category is not None:
        include = active_category.family()

    categories = [c for c in Category.objects.all() if c.depth() == 1 or
                                                       c in include]
    return {'sidenav_categories': categories}
