from django.conf.urls import patterns, include, url
from django.contrib import admin

import testing_app.urls

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DPL1.views.testing_app', name='testing_app'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^testing/',
                           include(testing_app.urls, app_name='testing_app'))
)
