from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from .models import PositionPionerUser
from .forms import PionerUserRegisterForm, PionerUserLoginForm, PionerUserEditForm


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_pioneruser_form = PionerUserRegisterForm(request.POST)
        if register_pioneruser_form.is_valid():
            register_pioneruser_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_pioneruser_form = PionerUserRegisterForm()

    context = {
        'title': title,
        'register_pioneruser_form': register_pioneruser_form,
    }

    return render(request, 'authapp/register.html', context=context)


def login(request):
    title = 'Вход'

    login_form = PionerUserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }

    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def edit(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_pioneruser_form = PionerUserEditForm(request.POST, instance=request.user)
        if edit_pioneruser_form.is_valid():
            edit_pioneruser_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_pioneruser_form = PionerUserEditForm(instance=request.user)

    context = {
        'title': title,
        'edit_pioneruser_form': edit_pioneruser_form,
    }

    return render(request, 'authapp/edit.html', context=context)


def rights_checking(request):
    position = PositionPionerUser.objects.filter(id=request.user.position_id).values('is_timetable_manager',
                                                                                     'is_methodist',
                                                                                     'is_teacher')
    return JsonResponse(*position)
