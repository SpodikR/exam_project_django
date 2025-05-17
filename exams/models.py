# exams/models.py
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва предмету")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

class Ticket(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="tickets", verbose_name="Предмет")
    number = models.CharField(max_length=50, verbose_name="Номер білету") # Може бути не тільки число, а "Білет №1", "Додатковий 1"

    def __str__(self):
        return f"{self.subject.name} - Білет {self.number}"

    class Meta:
        verbose_name = "Білет"
        verbose_name_plural = "Білети"
        ordering = ['subject', 'number'] # Для сортування

class Question(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="questions", verbose_name="Білет")
    question_text = models.TextField(verbose_name="Текст питання")
    answer_text = models.TextField(verbose_name="Текст відповіді")

    def __str__(self):
        return f"Питання до {self.ticket} (перші 30 символів: {self.question_text[:30]}...)"

    class Meta:
        verbose_name = "Питання"
        verbose_name_plural = "Питання"
