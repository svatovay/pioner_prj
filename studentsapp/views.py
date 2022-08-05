from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Student
from .forms import StudentForm


@login_required
def students(request):
    students = Student.objects.all().order_by('first_name')

    context = {
        'title': 'обучающиеся',
        'students': students,
    }

    return render(request, 'studentsapp/students.html', context=context)


@login_required
def student_create(request):
    title = 'Создание карточки обучающегося'

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect('/students/')
    else:
        student_form = StudentForm()

    context = {
        'title': title,
        'student_form': student_form,
    }

    return render(request, 'studentsapp/student_create.html', context=context)


@login_required
def student_edit(request, pk):
    edit_student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=edit_student)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect(reverse('studentsapp:student_edit', args=[edit_student.pk]))
    else:
        student_form = StudentForm(instance=edit_student)

    context = {
        'title': f'{edit_student.first_name} {edit_student.last_name}',
        # 'student': edit_student,
        'student_form': student_form,
    }

    return render(request, 'studentsapp/student_edit.html', context=context)
