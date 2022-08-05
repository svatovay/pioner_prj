from django.shortcuts import render


def timetables(request):
    # eduprograms = EduProgram.objects.all().order_by('id')

    context = {
        'title': 'Расписание',
        # 'eduprograms': eduprograms,
    }

    return render(request, 'timetableapp/timetables.html', context=context)


def timetable_create(request):
    title = 'Создание расписания группы'
    time_slots = (
        '08:00-08:45',
        '08:55-09:40',
        '09:50-10:35',
        '10:45-11:30',
        '11:40-12:25',
        '12:35-13:20',
        '13:30-14:15',
        '14:25-15:10',
        '15:20-16:05',
        '16:15-17:00',
        '17:10-17:55',
        '18:05-18:50',
        '19:00-19:45',
    )

    working_days = (
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье',
    )

    # if request.method == 'POST':
    #     eduprogram_form = EduProgramForm(request.POST)
    #     if eduprogram_form.is_valid():
    #         eduprogram_form.save()
    #         return HttpResponseRedirect('/eduprograms/')
    # else:
    #     eduprogram_form = EduProgramForm()

    context = {
        'title': title,
        'time_slots': time_slots,
        'working_days': working_days,
        # 'eduprogram_form': eduprogram_form,
    }

    return render(request, 'timetableapp/timetable_create.html', context=context)


def timetable_edit(request, pk):
    # edit_eduprogram = get_object_or_404(EduProgram, pk=pk)
    #
    # if request.method == 'POST':
    #     eduprogram_form = EduProgramForm(request.POST, instance=edit_eduprogram)
    #     if eduprogram_form.is_valid():
    #         eduprogram_form.save()
    #         return HttpResponseRedirect(reverse('eduprogramsapp:eduprogram_edit', args=[edit_eduprogram.pk]))
    # else:
    #     eduprogram_form = EduProgramForm(instance=edit_eduprogram)
    #
    # context = {
    #     'title': edit_eduprogram.name,
    #     # 'eduprogram': edit_eduprogram,
    #     'eduprogram_form': eduprogram_form,
    # }
    #
    # return render(request, 'eduprogramsapp/eduprogram_edit.html', context=context)
    pass
