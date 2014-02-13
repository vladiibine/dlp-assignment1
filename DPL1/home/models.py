from django.db import models

# Create your models here.
SEQUENCE = "the sequence of appearance in the test"


class Test(models.Model):
    name = models.CharField("test name", max_length=100)
    description = models.CharField("description", max_length=500, null=True)


class Page(models.Model):
    test = models.ForeignKey(Test)
    sequence = models.IntegerField(
        name=SEQUENCE, null=True)


class Question(models.Model):
    page = models.ForeignKey(Page)
    text = models.CharField(name="the question", max_length=100)
    sequence = models.IntegerField(name=SEQUENCE, null=True)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(name="an answer to a question", max_length=50)
    good_answer = models.BooleanField(name="whether this answer is acceptable",
                                      null=True)
    points = models.IntegerField(name="the number of points for this answer",
                                 null=True)