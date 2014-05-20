from django.core.urlresolvers import reverse
from django_webtest import WebTest
from dpl1_main.testing_app.models import Test
from dpl1_main.testing_app.models import Page, Question, Answer
from dpl1_main.testing_app.models import Result

__author__ = 'vardelean'


class TestWorkflow(WebTest):
    def setUp(self):
        self.t1 = Test.objects.create(name="test1", description="asdf")
        self.p1 = Page.objects.create(test=self.t1, sequence=2)
        self.q1 = Question.objects.create(page=self.p1, text="asdf?",
                                          sequence=1)
        self.a1 = Answer.objects.create(question=self.q1, text="Answer 1!",
                                        points=10)
        self.a2 = Answer.objects.create(question=self.q1, text="Answer 2!",
                                        points=20)

    def test_results_not_available(self):
        path = reverse('pages',
                       kwargs={'test_id': self.t1.id,
                               'page_id': self.t1.first_page()})
        form = self.app.get(path).form

        form[self.q1.as_form_id()] = unicode(self.a1.id)
        response = form.submit().follow()

        self.assertTrue(
            'testing_app/results_unavailable.html' in [template.name for
                                                       template in
                                                       response.templates])
        print "end"

    def test_results_available(self):
        self.r1 = Result.objects.create(test=self.t1, text="random result lol",
                                        description="doesn't matter",
                                        max_points=11)
        path = reverse('pages',
                       kwargs={'test_id': self.t1.id,
                               'page_id': self.t1.first_page()})

        form_p1 = self.app.get(path).form
        form_p1[self.q1.as_form_id()] = unicode(self.a1.id)

        response = form_p1.submit().follow()
        self.assertTrue(
            'testing_app/results.html' in [template.name for template in
                                           response.templates])