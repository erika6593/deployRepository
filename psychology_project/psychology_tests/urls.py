from django.urls import path
from django.contrib import admin
from .views import (
    QuizListView, QuizDetailView
)

app_name = 'psychology_tests'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz_list/', QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
]
# default_quiz_template1.html



