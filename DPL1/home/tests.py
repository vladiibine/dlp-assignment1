from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client

# Create your tests here.

#todo: Testezi aici response. (status_code, context, content, templates)
from home.models import Test, Page, Question, Answer, Result

Q_VERONICA_MICLE = "how's veronica micle"

Q_HOWS_VETA = "how's veta?"

ANSWER_3 = "answer3"
ANSWER_2 = "answer2"
ANSWER_1 = "answer1"
Q_ARE_YOU_SURE = "are you sure?"
TEST_1_NAME = "test 1"
TEST_1_DESCRIPTION = "test 1 lol"
RESULT_1_VERY_GOOD = "very good!"
RESULT_3_NO_DESCRIPTION = "no description - 3"
BAD = "bad!"
NO_DESCRIPTION_2 = "no description - 2"
NO_DESCRIPTION_1 = "no description - 1"
ALMOST_GOOD = "almost good!"


class TestAbstract(TestCase):
    def setUp(self):
        self.test1 = Test.objects.create(name=TEST_1_NAME,
                                         description=TEST_1_DESCRIPTION)
        self.t1_result1 = Result.objects.create(test=self.test1,
                                                text=RESULT_1_VERY_GOOD,
                                                description=NO_DESCRIPTION_1,
                                                max_points=1000)
        self.t1_result2 = Result.objects.create(test=self.test1,
                                                text=ALMOST_GOOD,
                                                description=NO_DESCRIPTION_2,
                                                max_points=99)
        self.t1_result3 = Result.objects.create(test=self.test1, text=BAD,
                                                description=RESULT_3_NO_DESCRIPTION,
                                                max_points=10)
        self.t1_page1 = Page.objects.create(test=self.test1, sequence=1)
        self.t1_p1_question1 = Question.objects.create(page=self.t1_page1,
                                                       text=Q_ARE_YOU_SURE,
                                                       sequence=1,
                                                       multiple_answers=0)
        self.t1_p1_q1_answer1 = Answer.objects.create(
            question=self.t1_p1_question1,
            text=ANSWER_1,
            points=1)
        self.t1_p1_q1_answer2 = Answer.objects.create(
            question=self.t1_p1_question1,
            text=ANSWER_2,
            points=10)
        self.t1_p1_q1_answer3 = Answer.objects.create(
            question=self.t1_p1_question1,
            text=ANSWER_3,
            points=100)

        #page with no questions
        self.t1_page2 = Page.objects.create(test=self.test1, sequence=2)

        #page with questions, but no answers
        self.t1_page3 = Page.objects.create(test=self.test1, sequence=3)
        self.t1_p3_q1 = Question.objects.create(page=self.t1_page3,
                                                text=Q_HOWS_VETA, sequence=1,
                                                multiple_answers=0)

        #page with questions and answers
        self.t1_p4 = Page.objects.create(test=self.test1, sequence=4)
        self.t1_p4_q1 = Question.objects.create(page=self.t1_p4,
                                                text=Q_VERONICA_MICLE,
                                                sequence=1, multiple_answers=1)
        self.t1_p4_q1_a1 = Answer.objects.create(question=self.t1_p4_q1,
                                                 text=ANSWER_1, points=4)
        self.t1_p4_q1_a2 = Answer.objects.create(question=self.t1_p4_q1,
                                                 text=ANSWER_2, points=90)

        #third page with valid answers
        self.t1_p5 = Page.objects.create(test=self.test1, sequence=5)
        self.t1_p5_q1 = Question.objects.create(page=self.t1_p5,
                                                text=Q_VERONICA_MICLE,
                                                sequence=1, multiple_answers=1)
        self.t1_p5_q1_a1 = Answer.objects.create(question=self.t1_p5_q1,
                                                 text=ANSWER_1, points=4)
        self.t1_p5_q1_a2 = Answer.objects.create(question=self.t1_p5_q1,
                                                 text=ANSWER_2, points=90)

    def _get_response(self, view_name='pages', **kwargs):
        client = Client()
        path = reverse(view_name, kwargs=kwargs)
        response = client.get(path)
        return response


class HomeTest(TestAbstract):
    def test_home_200(self):
        """Check if home page works with a few tests available
        """
        response = self._get_response('home')
        self.assertEqual(200, response.status_code)

    def test_home_empty(self):
        """Check if home page works empty
        """
        Test.objects.all().delete()
        response = self._get_response('home')
        self.assertTrue(
            'Welcome to the awesomest testing site' in response.content)

    def test_home_has_answers(self):
        response = self._get_response("home")
        self.assertTrue(TEST_1_NAME in response.content)


class PagesTest(TestAbstract):
    fixtures = ['initial_data']

    def test_first_page(self):
        response = self._get_response(test_id=self.test1.id,
                                      page_id=self.t1_page1.id)
        self.assertTrue(Q_ARE_YOU_SURE in response.content)

    def test_answers_on_page(self):
        response = self._get_response(test_id=self.test1.id,
                                      page_id=self.t1_page1.id)
        self.assertTrue(ANSWER_1 in response.content)
        self.assertTrue(ANSWER_2 in response.content)
        self.assertTrue(ANSWER_3 in response.content)

    def test_invalid_first_page(self):
        response = self._get_response(test_id=self.test1.id,
                                      page_id=self.t1_page2.id)
        # self.assertTrue(response.request['PATH_INFO'] == reverse('home'))
        self.assertEqual(response.request['PATH_INFO'], reverse('home'))