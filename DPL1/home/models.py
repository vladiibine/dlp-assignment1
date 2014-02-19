"""The Models for the application: This includes everything needed to run
    tests.
"""
from django.db import models

# Create your models here.


class Test(models.Model):
    """Model for the test.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return u"{0:s}".format(self.name)

    def __unicode__(self):
        return str(self)

    @classmethod
    def get_first_page_for(cls, test_id):
        """Return the first page for test, or None

        :param test_id: the id of the home.models.Test
        """
        test = cls.objects.filter(id=test_id)
        if test.count() < 1:
            return

        for page in test.get().page_set.all():
            if page.question_set.count() > 0:
                return page.id

    def first_page(self):
        """returns the first page for the current test
        :return:
        """
        return self.__class__.get_first_page_for(self.id)


class Page(models.Model):
    """Model for the Page.

    Pages are included in a test, in a sequential order
    """
    test = models.ForeignKey(Test)
    sequence = models.IntegerField()

    def __str__(self):
        return u"{0:s} - Page {1:d}".format(self.test, self.sequence)

    def __unicode__(self):
        return str(self)


class Question(models.Model):
    """Model for the Question.

    Questions are included in a page, in a sequential order
    """
    page = models.ForeignKey(Page)
    text = models.CharField(max_length=100)
    sequence = models.IntegerField(null=True)
    multiple_answers = models.BooleanField(default=0)

    def __str__(self):
        return u"{0:s} - Question : {1:s}".format(self.page, self.text)


class Answer(models.Model):
    """Model for the Answer.

    An answer is tied to a question. It can be a good or bad answer and it
    has a number of points attached to it.
    """
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=50)
    points = models.IntegerField()

    def __unicode__(self):
        return u"{0:s}".format(self.text)


class Result(models.Model):
    """Result for a Test.

    Contains the description of the result of a test, for a point maximum.
    """
    test = models.ForeignKey(Test)
    text = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    max_points = models.IntegerField(default=0, null=True, blank=True)

    def __unicode__(self):
        return u"{0:s}".format(self.text)