from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client

# Create your tests here.


class ResultTest(TestCase):
    def test_no_result(self):
        client = Client()
        response = client.get(reverse('home'))
        print 'lol'
