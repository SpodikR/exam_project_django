# exam_project/urls.py
from django.contrib import admin
from django.urls import path, include # Додай include
from django.conf import settings # Імпортуємо settings
from django.conf.urls.static import static # Імпортуємо static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exams.urls')), # <--- ДОДАЙ ЦЕЙ РЯДОК. Всі запити на головну сторінку підуть в exams.urls
]

# Додаємо це тільки якщо DEBUG=True (тобто під час розробки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Також можна додати для статичних файлів, якщо ти не використовуєш collectstatic під час розробки
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)