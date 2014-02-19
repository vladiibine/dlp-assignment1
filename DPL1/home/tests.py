from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client

# Create your tests here.


# class ResultTest(TestCase):
#     def test_no_result(self):
#         client = Client()
#         response = client.get(reverse('home'))
#todo: Testezi aici response. (status_code, context, content, templates)
from home.models import Test, Page, Question, Answer, Result

ANSWER_3 = "answer3"

ANSWER_2 = "answer2"

ANSWER_1 = "answer1"

Q_ARE_YOU_SURE = "are you sure?"

TEST_NAME = "test 1"

TEST_DESCRIPTION = "test 1 lol"

VERY_GOOD = "very good!"

NO_DESCRIPTION_3 = "no description - 3"

BAD = "bad!"

NO_DESCRIPTION_2 = "no description - 2"

NO_DESCRIPTION_1 = "no description - 1"

ALMOST_GOOD = "almost good!"


class TestAbstract(TestCase):
    def setUp(self):
        self.test = Test.objects.create(name=TEST_NAME,
                                        description=TEST_DESCRIPTION)
        self.result1 = Result.objects.create(test=self.test, text=VERY_GOOD,
                                             description=NO_DESCRIPTION_1,
                                             max_points=1000)
        self.result2 = Result.objects.create(test=self.test, text=ALMOST_GOOD,
                                             description=NO_DESCRIPTION_2,
                                             max_points=99)
        self.result3 = Result.objects.create(test=self.test, text=BAD,
                                             description=NO_DESCRIPTION_3,
                                             max_points=10)

        self.page = Page.objects.create(test=self.test, sequence=1)
        self.question = Question.objects.create(page=self.page,
                                                text=Q_ARE_YOU_SURE,
                                                sequence=1,
                                                multiple_answers=0)
        self.answer1 = Answer.objects.create(question=self.question,
                                             text=ANSWER_1,
                                             points=1)
        self.answer2 = Answer.objects.create(question=self.question,
                                             text=ANSWER_2,
                                             points=10)
        self.answer3 = Answer.objects.create(question=self.question,
                                             text=ANSWER_3,
                                             points=100)


class HomeTest(TestAbstract):
    def test_home_empty(self):
        """Check if home page works empty
        """
        Test.objects.all().delete()
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        self.assertTrue(
            'Welcome to the awesomest testing site' in response.content)

    def test_home_not_empty(self):
        """Check if home page works with a few tests available
        """
        pass


class ResultTest(TestAbstract):
    fixtures = ['initial_data']

    def _get_response(self):
        client = Client()
        path = reverse('pages', kwargs={'test_id': self.test.id,
                                        'page_id': self.page.id})
        response = client.get(path)
        return response

    def test_first_page(self):
        response = self._get_response()
        self.assertTrue(Q_ARE_YOU_SURE in response.content)

    def test_answers_on_page(self):
        response = self._get_response()
        self.assertTrue(ANSWER_1 in response.content)
        self.assertTrue(ANSWER_2 in response.content)
        self.assertTrue(ANSWER_3 in response.content)


