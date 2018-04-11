from django.contrib import admin

from .models import Questions, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionAdmin)
