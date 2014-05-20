from rest_framework import serializers
from dpl1_main.testing_app.models import Result, Test


class ResultHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result


class TestHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test