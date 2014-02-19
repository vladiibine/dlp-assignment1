"""Functions and decorators used by the views (`home.views`)
"""
import functools

from django.http import HttpResponseRedirect

from home.models import Page
from home.session_util import TestSession


def disable_navigation(func):
    """Disables navigation for a view

    :param func:
    :return:
    """

    def wrapper(request, *args, **kwargs):
        """Redirects to current page

        :param request:
        :param args:
        :param kwargs:
        """
        #determine where we came from
        return render_last_page(request)

    return wrapper


def is_page_sequence_valid(request, test_id, page_id, referer):
    """Checks whether the current test page is in the right sequence with
    regards to the last.

    Given the current test_id and page_id, this function checks the
    HTTP_REFERER (last page) to see if

    :param referer:
    """
    # test_session = request.session.get('test_session', None)
    test_session = TestSession(request.session)
    if test_session is None:
        raise KeyError('Unable to determine page sequence')

    last_test_id, last_page_id = test_session.get_last_test_page()
    if last_page_id is None and last_page_id is None:
        return page_id == 1

    if last_test_id != test_id:
        return False
    if page_id != get_next_page(last_test_id, last_page_id):
        return False


def get_last_rel_url(request):
    """Returns the relative URL of the last page (the referer)
    :param request: the request obj
    """
    return request.META.get('HTTP_REFERER')


def render_last_page(request):
    """Returns a request for the last page

    :param request:
    """
    referer_url = request.META.get('HTTP_REFERER')
    response = HttpResponseRedirect(referer_url)

    return response


def validate_navigation(func):
    """Decorator: Makes sure the workflow of the home application is respected.

    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        """
        :param kwargs:
        :param args:
        :param request:
        """
        #check if the current page is a valid successor for the test pages
        referer = get_last_rel_url(request)

        test_id = kwargs.get('test_id', None)
        page_id = kwargs.get('page_id', None)

        if not (test_id is None or page_id is None):
            if is_page_sequence_valid(request, test_id, page_id, referer):
                result = func(request, *args, **kwargs)
                return result
            else:
                return render_last_page(request)

        #todo: check if the form was validated
        if 0 == 0:
            pass

        #todo allow access from the home page to any /tests/x/<get_first_page>

    return wrapper


def get_next_page(test_id, page_id):
    """Determines the next test page.

    Either the next page in the test that has questions,
        or 0 - meaning the results page.
    :param page_id: id of the home.models.Page
    :param test_id: if of the home.models.Test
    """
    next_pages = Page.objects.filter(id__gt=page_id, test__id=test_id)

    for page in next_pages:
        if page.question_set.count() > 0:
            return page.id
    else:
        return 0


def save_answers(func):
    """Updates the session with the answers from the form on the last page.
    :param func: function being decorated
    """

    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        """Wraps the function to be decorated

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        test_id = kwargs.get('test_id', None)
        page_id = kwargs.get('page_id', None)
        test_session = TestSession(request.session)
        test_session.test_id = test_id
        test_session.update_results(request.POST, page_id)
        return func(request, *args, **kwargs)

    return wrapper


