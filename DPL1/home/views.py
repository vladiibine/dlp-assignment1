"""Define the views used in the application `home`
"""
import itertools

from django.core.urlresolvers import reverse
from django.shortcuts import render
import django.http

from home.forms import create_form_for_questions
from home.models import Test, Answer, Result, Question
from home.view_util import get_next_page, save_answers


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
    return render(request, 'questionnaire/asdf.html',
                  {'form': form, 'pages': pages})


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
    request.session.get('answers', {}).clear()
    request.session.save()
    context = {'tests': tests}
    result = render(request, 'questionnaire/index.html', context)
    return result


@save_answers
def show_result_view(request, test_id):
    """Shows the results page for the corresponding test_id
    :param test_id: id of the home.models.Test
    :param request:
    """
    #1 calculate the result for the given test ID
    session = request.session
    answers = session.get('answers', {})
    answer_lists = (answers[question] for question in
                    answers.keys() if 'question' in question)
    answer_ids = itertools.chain(*answer_lists)
    answers = Answer.objects.filter(id__in=answer_ids)
    total_points = 0
    for answer in answers:
        total_points += answer.points

    #2 compare with test results
    test_results = Result.objects.filter(
        max_points__lte=total_points, test__id=test_id).order_by('-max_points')
    context = {}
    if test_results.count() > 0:
        context['result'] = test_results[0]
    else:
        context['no_results'] = True

    context['home_url'] = request.build_absolute_uri(reverse('home'))

    return render(request, 'questionnaire/results.html', context)


@save_answers
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