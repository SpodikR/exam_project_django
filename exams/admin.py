# exams/admin.py
from django.contrib import admin
from .models import Subject, Ticket, Question

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'subject')
    list_filter = ('subject',) # Фільтр по предмету
    search_fields = ('number', 'subject__name')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'short_question_text', 'short_answer_text')
    list_filter = ('ticket__subject', 'ticket') # Фільтр по предмету та білету
    search_fields = ('question_text', 'answer_text', 'ticket__number', 'ticket__subject__name')

    def short_question_text(self, obj):
        return obj.question_text[:70] + "..." if len(obj.question_text) > 70 else obj.question_text
    short_question_text.short_description = "Питання (коротко)"

    def short_answer_text(self, obj):
        return obj.answer_text[:70] + "..." if len(obj.answer_text) > 70 else obj.answer_text
    short_answer_text.short_description = "Відповідь (коротко)"

# Або простіше, якщо не потрібні кастомні налаштування:
# admin.site.register(Subject)
# admin.site.register(Ticket)
# admin.site.register(Question)
