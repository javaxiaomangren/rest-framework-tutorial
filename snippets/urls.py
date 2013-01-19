from django.conf.urls import patterns, url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

# API endpoints
urlpatterns = format_suffix_patterns(patterns('snippets.views',
    url(r'^$', 'api_root'),
))
