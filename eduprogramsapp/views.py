from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import EduProgram
from .forms import EduProgramForm


@login_required
def eduprograms(request):
    eduprograms = EduProgram.objects.all().order_by('id')

    context = {
        'title': 'Образовательные программы',
        'eduprograms': eduprograms,
    }

    return render(request, 'eduprogramsapp/eduprograms.html', context=context)


@login_required
def eduprogram_create(request):
    title = 'Создание ДОП'

    if request.method == 'POST':
        eduprogram_form = EduProgramForm(request.POST)
        if eduprogram_form.is_valid():
            new_eduprogram = eduprogram_form.save(commit=False)
            eduprogram_form.save()
            return HttpResponseRedirect(reverse('eduprogramsapp:eduprogram_edit', args=[new_eduprogram.pk]))
    else:
        eduprogram_form = EduProgramForm()

    context = {
        'title': title,
        'eduprogram_form': eduprogram_form,
    }

    return render(request, 'eduprogramsapp/eduprogram_create.html', context=context)


@login_required
def eduprogram_edit(request, pk):
    edit_eduprogram = get_object_or_404(EduProgram, pk=pk)

    if request.method == 'POST':
        eduprogram_form = EduProgramForm(request.POST, instance=edit_eduprogram)
        if eduprogram_form.is_valid():
            eduprogram_form.save()
            return HttpResponseRedirect(reverse('eduprogramsapp:eduprogram_edit', args=[edit_eduprogram.pk]))
    else:
        eduprogram_form = EduProgramForm(instance=edit_eduprogram)

    context = {
        'title': edit_eduprogram.name,
        'eduprogram_form': eduprogram_form,
    }

    return render(request, 'eduprogramsapp/eduprogram_edit.html', context=context)
