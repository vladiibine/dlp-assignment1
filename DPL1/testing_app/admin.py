from django.contrib import admin

import testing_app.models

# Register your models here.


class PageInline(admin.TabularInline):
    model = testing_app.models.Page


class QuestionInline(admin.TabularInline):
    model = testing_app.models.Question


class AnswerInline(admin.TabularInline):
    model = testing_app.models.Answer


class ResultInline(admin.TabularInline):
    model = testing_app.models.Result


class TestAdmin(admin.ModelAdmin):
    inlines = (PageInline, ResultInline)
    list_display = ('name', 'description')


class PageAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    ordering = ('test', 'sequence')


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    ordering = ('page', 'text')


admin.site.register(testing_app.models.Test, TestAdmin)
admin.site.register(testing_app.models.Page, PageAdmin)
admin.site.register(testing_app.models.Question, QuestionAdmin)