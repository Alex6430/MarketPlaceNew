from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response

def admin(request):
    return render(request, 'admin')


def account_view(request):
    # если это суперпользователь
    if request.user.is_superuser:
        return redirect('admin')
    # или если это пользователь с галочкой персонал, а так же принадлежащий группе manager
    elif request.user.groups.filter(name='Manager').exists():
        template = 'Market/Manager.html'
    # или если это пользователь принадлежащий группе manager
    elif request.user.groups.filter(name='Courier').exists():
        template = 'Registration/homePage.html'
    # иначе все остальные (обычные пользователи)
    else:
        template = 'Registration/homePage.html'

    return render(request, template)