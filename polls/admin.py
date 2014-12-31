from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInLine]

    list_filter = ['pub_date']

    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
