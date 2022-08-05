from django.urls import path
from .views import eduprograms, eduprogram_edit, eduprogram_create

app_name = 'eduprogramsapp'

urlpatterns = [
    path('', eduprograms, name='index'),
    path('eduprogram/create/', eduprogram_create, name='eduprogram_create'),
    path('eduprogram/edit/<int:pk>/', eduprogram_edit, name='eduprogram_edit'),
]
