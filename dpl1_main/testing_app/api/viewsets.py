from rest_framework import viewsets
from dpl1_main.testing_app.api.serializers import (ResultHyperlinkSerializer,
                                                   TestHyperlinkedSerializer,
                                                   ResultSerializer)
from dpl1_main.testing_app.models import Result, Test


class ResultViewset(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request, *args, **kwargs):
        result = super(ResultViewset, self).list(request, *args, **kwargs)
        return result


class TestViewset(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestHyperlinkedSerializer