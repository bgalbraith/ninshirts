from apps.catalog.models import Category

def sidenav(request):
    """Generate the appropriate sidebar navigation expansion."""
    categories = Category.objects.all()
    return {'sidenav_categories': categories}
