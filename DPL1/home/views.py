from django.shortcuts import render
from home.forms import PageForm
from home.models import Test, Page, Question, Answer
import django.http
from django.template import loader, RequestContext
# Create your views here.

def test_view(request):
    #atm testing forms
    # return django.http.HttpResponse("Hello world. Vlad was here!!!")
    form = PageForm(request.POST)
    return render(request, 'questionaire/asdf.html', {'form': form})


def error_view(request):
    return django.http.Http404()


def home_view(request):
    #instantiate the template in the dir given (project dir - cuz
    # of TEMPLATES_DIR ) name in the settings module of the project
    template = loader.get_template('questionaire/index.html')
    #create the context for the view - just fill the list of crap here
    tests = Test.objects.all()
    context = RequestContext(request, {'tests': tests})
    # return django.http.HttpResponse(template.render(context))

    #do the above, quicker
    return render(request, 'questionaire/index.html', {'tests': tests})


def pages_view(request, test_id, page_id=1):
    test = Test.objects.get(id=test_id)
    page = Page.objects.get(id=page_id)
    questions = Question.objects.filter(page__test_id=test_id, page_id=page_id)
    form_id = "form%i_%i" % (test.id, page.id)
    return render(request, 'questionaire/test_page.html',
                  {'questions': questions, 'page': page, 'test': test,
                   'form_id': form_id})