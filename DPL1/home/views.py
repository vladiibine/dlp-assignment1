from django.shortcuts import render
import django.http
from django.template import loader, RequestContext
from home.forms import create_form_for_page

from home.models import Test, Page, Question

# Create your views here.

def test_view(request):
    #atm testing forms
    # return django.http.HttpResponse("Hello world. Vlad was here!!!")
    # form = PageForm(request.POST)
    #tre sa returnez o clasa DynamicPageForm care sa contina toata randarea
    # formului, pt toata pagina, si gata.
    test = Test.objects.get(id=4)

    form = create_form_for_page()
    pages = test.page_set
    return render(request, 'questionaire/asdf.html',
                  {'form': form, 'pages': pages})


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


def show_result_view(request, test_id):
    pass


def pages_view(request, test_id, page_id=1):
    if page_id == 0:
        return show_result_view(request, test_id)
    test = Test.objects.get(id=test_id)
    page = Page.objects.get(id=page_id)
    questions = Question.objects.filter(page__test_id=test_id, page_id=page_id)
    next_pages = Page.objects.filter(id__gt=page_id)
    if next_pages.count() == 1:
        next_page_id = next_pages[1].id
    else:
        next_page_id = 0
    form = create_form_for_page(questions)
    return render(request, 'questionaire/test_page.html',
                  {'questions': questions, 'page': page, 'test': test,
                   'next_page_id': next_page_id, 'form': form})



