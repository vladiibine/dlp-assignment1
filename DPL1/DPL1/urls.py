from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DPL1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', views.home_view, name='home'),
    url(r'^tests/(?P<test_id>\d+)', views.pages_view, name='pages'),
    url(r'^tests/(?P<test_id>\d+)/(?P<page_id>\d+)', views.pages_view, name='pages'),
    url(r'^404', views.error_view, name='error'),
    url(r'^asdf$', views.test_view, name='test'),
)
