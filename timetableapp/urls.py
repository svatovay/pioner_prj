from django.urls import path
from .views import timetables, timetable_create, timetable_edit

app_name = 'timetableapp'

urlpatterns = [
    path('', timetables, name='index'),
    path('create/', timetable_create, name='timetable_create'),
    path('edit/<int:pk>/', timetable_edit, name='timetable_edit'),
]