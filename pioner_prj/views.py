from django.shortcuts import render


def index(request):
    context = {
        'title': 'главная',
    }

    return render(request, 'pioner_prj/index.html', context=context)


def contacts(request):
    context = {
        'title': 'контакты',
    }

    return render(request, 'pioner_prj/contacts.html', context=context)
