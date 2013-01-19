from django.conf.urls import patterns, url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

# API endpoints
urlpatterns = format_suffix_patterns(patterns('snippets.views',
    url(r'^$', 'api_root'),
))

# Login and logout views for the browsable API
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
)
