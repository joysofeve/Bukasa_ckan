from django.conf.urls import patterns, url

from geonode.urls import *

from django.views.generic import RedirectView

urlpatterns = patterns('',

    # Static pages
#    url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),
    url(r'^$', RedirectView.as_view(url='/dataset/')),
 ) + urlpatterns

