# exams/views.py
from django.shortcuts import render, get_object_or_404
from .models import Subject, Ticket, Question

def subject_list_view(request):
    subjects = Subject.objects.all().prefetch_related('tickets') # prefetch_related для оптимізації
    context = {
        'subjects': subjects
    }
    return render(request, 'exams/subject_list.html', context)

def ticket_list_view(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    tickets = Ticket.objects.filter(subject=subject).prefetch_related('questions') # prefetch_related для оптимізації
    context = {
        'subject': subject,
        'tickets': tickets
    }
    return render(request, 'exams/ticket_list.html', context)

def ticket_detail_view(request, ticket_id):
    ticket = get_object_or_404(Ticket.objects.select_related('subject').prefetch_related('questions'), id=ticket_id)
    # select_related('subject') для оптимізації доступу до subject.name
    # prefetch_related('questions') для оптимізації доступу до ticket.questions.all
    context = {
        'ticket': ticket
    }
    return render(request, 'exams/ticket_detail.html', context)
