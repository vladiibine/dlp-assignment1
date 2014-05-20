from django.conf.urls import patterns, url, include
from rest_framework import routers
from dpl1_main.testing_app.api.viewsets import ResultViewset, TestViewset


class Testing_AppApiRouter(routers.SimpleRouter):
    pass



api_router = Testing_AppApiRouter()

api_router.register('results', ResultViewset)
api_router.register('tests', TestViewset)


print ">>>VWH:::"

print "<<<<"

urlpatterns = patterns('',
       url(r'asdf/(?P<call_sign>\w+)/', include(api_router.urls)),
)