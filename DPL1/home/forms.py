from django import forms


def create_form_for_questions(questions):
    """Creates a dynamic form instance, given the questions in a page

    :param questions: django.db.models.QuerySet of home.models.Question
    :return: django.forms.Form instance
    """
    bases = (forms.Form,)
    attributes = {}
    if questions.count() == 0:
        attributes["submittable"] = False
        return type("EmptyDynamicForm", bases, attributes)
    for question in questions.all():
        choices = []
        for answer in question.answer_set.all():
            choices.append((answer.id, answer.text))
        if question.multiple_answers is True:
            widget = forms.CheckboxSelectMultiple
        else:
            widget = forms.RadioSelect
        attributes["question_%i" % question.id] = (
            forms.ChoiceField(widget=widget,
                              choices=choices,
                              label=question.text)
        )
    attributes['submittable'] = True
    form = type("DynamicPageForm", bases, attributes)
    return form()
