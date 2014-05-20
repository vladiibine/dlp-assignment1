from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.admin import sites

from dpl1_main.testing_app import views


class CustomAdmin(sites.AdminSite):
    login_template = 'testing_app/admin/login.html'


admin.site = CustomAdmin()
admin.autodiscover()

urlpatterns = patterns('testing_app',
                       # Examples:
                       # url(r'^$', 'DLP.views.testing_app',
                       # name='testing_app'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls),
                           name='admin'),
                       # url(r'^admin/', include(admin.site.urls),
                       # name='admin'),
                       url(r'^$', views.home_view, name='testing_app'),
                       url(r'tests/(?P<test_id>\d+)/results',
                           views.show_result_view, name='results'),
                       url(r'^tests/(?P<test_id>\d+)/(?P<page_id>\d+)',
                           views.pages_view, name='pages'),
                       url(r'^404', views.error_view, name='error'),
                       url(r"^form/", views.form_view, name="form")
)
