from django.urls import path
from .views import students, student_create, student_edit

app_name = 'studentsapp'

urlpatterns = [
    path('', students, name='index'),
    path('student/create/', student_create, name='student_create'),
    path('student/edit/<int:pk>/', student_edit, name='student_edit'),
]
