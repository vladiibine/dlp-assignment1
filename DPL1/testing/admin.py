from django.contrib import admin

import testing.models

# Register your models here.


class PageInline(admin.TabularInline):
    model = testing.models.Page


class QuestionInline(admin.TabularInline):
    model = testing.models.Question


class AnswerInline(admin.TabularInline):
    model = testing.models.Answer


class ResultInline(admin.TabularInline):
    model = testing.models.Result


class TestAdmin(admin.ModelAdmin):
    inlines = (PageInline, ResultInline)
    list_display = ('name', 'description')


class PageAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    ordering = ('test', 'sequence')


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    ordering = ('page', 'text')


admin.site.register(testing.models.Test, TestAdmin)
admin.site.register(testing.models.Page, PageAdmin)
admin.site.register(testing.models.Question, QuestionAdmin)