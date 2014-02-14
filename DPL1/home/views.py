from django.shortcuts import render
import home.models
import django.http
from django.template import loader, RequestContext
# Create your views here.

def home_view(request):
    # return django.http.Http404("vwh, so all's well")
    return django.http.HttpResponse("Hello world. Vlad was here!!!")


def error_view(request):
    return django.http.Http404()


def test_view(request):
    #instantiate the template in the dir given (project dir - cuz
    # of TEMPLATES_DIR ) name in the settings module of the project
    template = loader.get_template('questionaire/index.html')
    #create the context for the view - just fill the list of crap here
    tests = home.models.Test.objects.all()
    context = RequestContext(request, {'tests': tests})
    return django.http.HttpResponse(template.render(context))