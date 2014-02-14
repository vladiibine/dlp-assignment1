from django import forms
from django.forms import widgets


class PageForm(forms.Form):
    # answers = forms.MultipleChoiceField((1, 2, 3, 6, 7, 8),
    #                                     widget=widgets.RadioInput)
    number = forms.IntegerField(6, 2)
    text = forms.CharField(20, 2)