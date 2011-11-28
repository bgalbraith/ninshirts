from django.conf.urls.defaults import patterns, include, url

# Uncomment the next line if running standalone development
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ninshirts.catalog.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<collection_tag>\w+)/$', 'ninshirts.catalog.views.collection'),
    url(r'^(?P<collection_tag>\w+)/(?P<shirt_tag>\w+)/$', 'ninshirts.catalog.views.shirt'),

    # Uncomment the next line if running standalone development
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
