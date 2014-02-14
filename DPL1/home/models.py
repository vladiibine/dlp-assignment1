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


class Page(models.Model):
    """Model for the Page.

    Pages are included in a test, in a sequential order
    """
    test = models.ForeignKey(Test)
    sequence = models.IntegerField()

    def __str__(self):
        return u"Pagina {0:d}".format(self.sequence)

    def __unicode__(self):
        return str(self)


class Question(models.Model):
    """Model for the Question.

    Questions are included in a page, in a sequential order
    """
    page = models.ForeignKey(Page)
    text = models.CharField(max_length=100)
    sequence = models.IntegerField(null=True)

    def __str__(self):
        return u"{0:s}".format(self.text)


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