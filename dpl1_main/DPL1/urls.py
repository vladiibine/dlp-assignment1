from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DLP.views.testing_app',
                       # name='testing_app'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^testing/',
                           include('dpl1_main.testing_app.urls',
                                   app_name='testing_app')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/', include('dpl1_main.testing_app.api.urls'),
                           name='testing_api')

)
