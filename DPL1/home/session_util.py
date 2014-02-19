import itertools
from home.models import Answer, Result


class TestSession(object):
    """Uses the session as a container for the test logic """

    def __init__(self, session):
        """Initializes the answers list
        """
        #todo - efectiv n-am nevoie de dict, ci de o lista de raspunsuri.
        self.answers = session.get('answers', {})
        self.test_id = session.get('test_id', None)
        self.page_id = session.get('page_id', None)
        self.last_page_id = self.last_test_id = None
        self.session = session

    def update_results(self, post_dict, test_id, page_id):
        """Update the answers list from the POST object of the request

        :param post_dict: the request.POST which contains the form data
        :param page_id: the id of the home.models.Page
        """
        form_dict = {key: post_dict.getlist(key) for key in post_dict if
                     'question' in key}
        self.answers.update(form_dict)
        self.last_page_id = self.page_id
        self.test_id = test_id
        self.session['test_id'] = test_id
        self.session['page_id'] = page_id
        self.page_id = page_id
        self.save_to_session()

    def get_test_result(self, test_id):
        """Return the test result that the user got, at the end of the test.

        :param test_id: id of the home.models.Test
        """
        answer_lists = (self.answers[question] for question in
                        self.answers.keys() if 'question' in question)
        answer_ids = itertools.chain(*answer_lists)
        answers = Answer.objects.filter(id__in=answer_ids)
        total_points = 0
        for answer in answers:
            total_points += answer.points

        test_results = Result.objects.filter(
            max_points__lte=total_points, test__id=test_id).order_by(
            '-max_points')
        #2 compare with test results
        if test_results.count() > 0:
            return test_results[0]
        else:
            return None

    def get_last_test_page(self):
        """Return the last test page that the user submitted.
        """
        return self.test_id, self.last_page_id

    def save_to_session(self):
        """Save the currently managed test data to the user session.
        """
        self.session['answers'] = self.answers
        self.session.save()

    def clear_answers(self):
        """Clears the answers of the previous user session."""
        self.session.clear()
        self.session.save()