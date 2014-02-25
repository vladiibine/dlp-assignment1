from django.conf.urls import patterns, include, url
from django.contrib import admin

import testing.urls

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DPL1.views.testing', name='testing'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^testing/',
                           include(testing.urls, app_name='testing'))
)
