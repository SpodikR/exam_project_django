# exams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list_view, name='subject_list'),
    path('subject/<int:subject_id>/tickets/', views.ticket_list_view, name='ticket_list'),
    path('ticket/<int:ticket_id>/', views.ticket_detail_view, name='ticket_detail'),
]
