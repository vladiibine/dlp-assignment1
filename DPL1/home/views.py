import functools
import itertools
from django.core.urlresolvers import reverse

from django.shortcuts import render
import django.http
from django.template import loader, RequestContext

from home.forms import create_form_for_questions
from home.models import Test, Page, Question, Answer, Result


# Create your views here.

def test_view(request):
    #atm testing forms
    # return django.http.HttpResponse("Hello world. Vlad was here!!!")
    # form = PageForm(request.POST)
    #tre sa returnez o clasa DynamicPageForm care sa contina toata randarea
    # formului, pt toata pagina, si gata.
    test = Test.objects.get(id=4)

    form = create_form_for_questions()
    pages = test.page_set
    return render(request, 'questionaire/asdf.html',
                  {'form': form, 'pages': pages})


def error_view(request):
    return django.http.Http404()


def home_view(request):
    #instantiate the template in the dir given (project dir - cuz
    # of TEMPLATES_DIR ) name in the settings module of the project
    #create the context for the view - just fill the list of crap here
    tests = Test.objects.all()
    request.session.get('answers', {}).clear()
    request.session.save()

    return render(request, 'questionaire/index.html', {'tests': tests})


def update_session(func):
    """Updates the session with the answers from the form on the last page.
    """

    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        session = request.session
        post_dict = request.POST
        form_dict = {key: post_dict.getlist(key) for key in post_dict if
                     'question' in key}
        answers = session.get('answers', {})
        answers.update(form_dict)
        session['answers'] = answers
        session.save()
        return func(request, *args, **kwargs)

    return wrapper


@update_session
def show_result_view(request, test_id):
    """Shows the results page for the corresponding test_id """
    #1 calculate the result for the given test ID
    session = request.session
    answers = session.get('answers', {})
    answer_lists = [answers[question] for question in
                    answers.keys() if 'question' in question]
    answer_ids = itertools.chain(*answer_lists)
    answer_ids_list = list(answer_ids)
    answers = Answer.objects.filter(id__in=answer_ids_list)
    total_points = 0
    for answer in answers:
        total_points += answer.points

    #2 compare with test results
    test_results = Result.objects.filter(
        max_points__lte=total_points).order_by(
        '-max_points')
    if test_results.count() > 0:
        result = test_results[0]

    home_url = request.build_absolute_uri(reverse('home'))

    context = {'result': result, 'home_url': home_url}
    return render(request, 'questionaire/results.html', context)


@update_session
def pages_view(request, test_id, page_id=1):
    """Handles the logic for the test pages view:
        "questionaire/test_page.html"
    """
    #Determine next page: either normal page, or results page
    next_pages = Page.objects.filter(id__gt=page_id)
    if next_pages.count() > 0 and next_pages[0].question_set.count() > 0:
        next_page_id = next_pages[0].id
    else:
        next_page_id = 0

    questions = Question.objects.filter(page__test_id=test_id,
                                        page_id=page_id)
    form = create_form_for_questions(questions)
    context = {'questions': questions, 'test_id': test_id,
               'next_page_id': next_page_id, 'form': form}
    if form.submittable is False:
        context['parent_url'] = request.META.get('HTTP_REFERER')

    return render(request, 'questionaire/test_page.html', context)



