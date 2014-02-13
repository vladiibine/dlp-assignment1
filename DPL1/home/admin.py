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
    # ordering = 1


class PageAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    list_display = ["get_name"]


class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)


admin.site.register(home.models.Test, TestAdmin)
admin.site.register(home.models.Page, PageAdmin)
admin.site.register(home.models.Question, QuestionAdmin)
