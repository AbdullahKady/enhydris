from django.conf.urls.defaults import patterns

from enhydris.hchartpages import views

urlpatterns = patterns('',

    (r'^(?P<urlcode>[^/]+)/$',
     views.chartpage_detail, {}, 'chartpage_detail'),
     
)
