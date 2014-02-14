from django.contrib import admin

import home.models

# Register your models here.


class PageInline(admin.TabularInline):
    model = home.models.Page


class QuestionInline(admin.TabularInline):
    model = home.models.Question


class AnswerInline(admin.TabularInline):
    model = home.models.Answer


class TestAdmin(admin.ModelAdmin):
    inlines = (PageInline,)
    list_display = ('name', 'description')
    # ordering = 1


class PageAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    ordering = ('sequence',)


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)


admin.site.register(home.models.Test, TestAdmin)
admin.site.register(home.models.Page, PageAdmin)
admin.site.register(home.models.Question, QuestionAdmin)
