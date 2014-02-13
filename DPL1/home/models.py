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


class Page(models.Model):
    """Model for the Page.

    Pages are included in a test, in a sequential order
    """
    test = models.ForeignKey(Test)
    sequence = models.IntegerField(null=True)

    def get_name(self):
        """Used for displaying the name of this entity

        :return:
        """
        return "Page number {0:s}".format(self.sequence)


class Question(models.Model):
    """Model for the Question.

    Questions are included in a page, in a sequential order
    """
    page = models.ForeignKey(Page)
    text = models.CharField(max_length=100)
    sequence = models.IntegerField(null=True)


class Answer(models.Model):
    """Model for the Answer.

    An answer is tied to a question. It can be a good or bad answer and it
    has a number of points attached to it.
    """
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=50)
    points = models.IntegerField()