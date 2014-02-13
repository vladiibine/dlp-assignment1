from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DPL1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home_view),
    url(r'^$', views.home_view),
)
