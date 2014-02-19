"""Define the views used in the application `home`
"""
from django.core.urlresolvers import reverse
from django.shortcuts import render
import django.http

from home.forms import create_form_for_questions
from home.models import Test, Answer, Result, Question
# from home.session_util import TestSession
from home.session_util import TestSession
from home.view_util import get_next_page, save_answers, validate_navigation


class TestCioban(object):
    prop = 4


def test_view(request):
    """Only used for testing.
    :param request:
    :return:
    """
    #atm testing forms
    # return django.http.HttpResponse("Hello world. Vlad was here!!!")
    # form = PageForm(request.POST)
    #tre sa returnez o clasa DynamicPageForm care sa contina toata randarea
    # formului, pt toata pagina, si gata.
    test = Test.objects.get(id=4)

    # form = create_form_for_questions()
    form = None
    pages = test.page_set
    TestCioban.prop += 1
    return render(request, 'questionnaire/asdf.html',
                  {'form': form, 'pages': pages, 'test': TestCioban})


def error_view(request):
    """The default error view
    :param request:
    :return:
    """
    return django.http.Http404()


def home_view(request):
    #instantiate the template in the dir given (project dir - cuz
    # of TEMPLATES_DIR ) name in the settings module of the project
    #create the context for the view - just fill the list of crap here
    """The view for the home page

    :param request:
    """
    tests = Test.objects.all()
    test_session = TestSession(request.session)
    test_session.clear_answers()
    context = {'tests': tests}
    result = render(request, 'questionnaire/index.html', context)
    return result


@save_answers
@validate_navigation
def show_result_view(request, test_id):
    """Shows the results page for the corresponding test_id
    :param test_id: id of the home.models.Test
    :param request:
    """
    context = {}
    test_session = TestSession(request.session)
    test_result = test_session.get_test_result(test_id)
    context['result'] = test_result
    if test_result is None:
        context['no_result'] = True

    context['home_url'] = request.build_absolute_uri(reverse('home'))
    return render(request, 'questionnaire/results.html', context)


@save_answers
@validate_navigation
def pages_view(request, test_id, page_id=1):
    """Handles the logic for the test pages view:
        "questionnaire/test_page.html"
        :param request
        :param test_id
        :param page_id
    """
    #Determine next page: either normal page, or results page
    next_page_id = get_next_page(test_id, page_id)

    questions = Question.objects.filter(page__test_id=test_id,
                                        page_id=page_id)
    form = create_form_for_questions(questions)
    context = {'test_id': test_id, 'next_page_id': next_page_id, 'form': form}
    if form.submittable is False:
        context['parent_url'] = request.META.get('HTTP_REFERER')

    result = render(request, 'questionnaire/test_page.html', context)
    return result