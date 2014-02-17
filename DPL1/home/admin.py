from django.contrib import admin

import home.models

# Register your models here.


class PageInline(admin.TabularInline):
    model = home.models.Page


class QuestionInline(admin.TabularInline):
    model = home.models.Question


class AnswerInline(admin.TabularInline):
    model = home.models.Answer


class ResultInline(admin.TabularInline):
    model = home.models.Result


class TestAdmin(admin.ModelAdmin):
    inlines = (PageInline, ResultInline)
    list_display = ('name', 'description')


class PageAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    ordering = ('test', 'sequence')


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    ordering = ('page', 'text')


admin.site.register(home.models.Test, TestAdmin)
admin.site.register(home.models.Page, PageAdmin)
admin.site.register(home.models.Question, QuestionAdmin)