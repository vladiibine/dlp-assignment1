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
    template = loader.get_template('questionaire/index.html')
    #create the context for the view - just fill the list of crap here
    tests = Test.objects.all()
    context = RequestContext(request, {'tests': tests})
    # return django.http.HttpResponse(template.render(context))

    #do the above, quicker
    return render(request, 'questionaire/index.html', {'tests': tests})


def show_result_view(request, test_id):
    """Shows the results page for the corresponding test_id """
    #1 calculate the result for the given test ID
    session = request.session
    answer_lists = (session[question] for question in session.keys() if
                    'question' in question)
    answer_ids = itertools.chain(*answer_lists)
    answers = Answer.objects.filter(id__in=answer_ids)
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


# @csrf_protect
def update_session(session, post_dict):
    """Updates the session with the answers from the form on the last page.
    """
    form_dict = {key: post_dict.getlist(key) for key in post_dict if
                 'question' in key}
    session.update(form_dict)


def pages_view(request, test_id, page_id=1):
    #Determine next page: either normal page, or results page
    next_pages = Page.objects.filter(id__gt=page_id)
    if next_pages.count() > 0 and next_pages[0].question_set.count() > 0:
        next_page_id = next_pages[0].id
    else:
        next_page_id = 0

    if int(page_id) > 1:
        update_session(request.session, request.POST)

    questions = Question.objects.filter(page__test_id=test_id,
                                        page_id=page_id)
    form = create_form_for_questions(questions)
    context = {'questions': questions, 'test_id': test_id,
               'next_page_id': next_page_id, 'form': form}
    if form.submittable is False:
        context['parent_url'] = request.META.get('HTTP_REFERER')

    return render(request, 'questionaire/test_page.html', context)



