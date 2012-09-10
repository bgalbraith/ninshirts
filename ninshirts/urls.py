from django.conf.urls import patterns, include, url
from ninshirts import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.catalog.views.index'),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the next two line if running the development server:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),

    url(r'^(?P<category_tag>[a-z0-9-]+)/$',
        'apps.catalog.views.category'),
    url(r'^(?P<category_tag>[a-z0-9-]+)/(?P<product_tag>[a-z0-9-]+)/$',
        'apps.catalog.views.product'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
