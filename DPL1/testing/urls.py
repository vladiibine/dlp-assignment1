from django.conf.urls import patterns, include, url
from django.contrib import admin

from testing import views

admin.autodiscover()

urlpatterns = patterns('testing',
                       # Examples:
                       # url(r'^$', 'DPL1.views.testing', name='testing'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls),
                           name='admin'),
                       url(r'^$', views.home_view, name='testing'),
                       url(r'tests/(?P<test_id>\d+)/results',
                           views.show_result_view, name='results'),
                       url(r'^tests/(?P<test_id>\d+)/(?P<page_id>\d+)',
                           views.pages_view, name='pages'),
                       url(r'^404', views.error_view, name='error'),
                       url(r'^asdf$', views.test_view, name='test'),
)
