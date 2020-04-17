from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from Registration.forms import MyUserForm


def admin(request):
    return render(request, 'admin')

def index(request):
    return render(request, 'Registration/homePage.html')

def auth_login(request):
    print("login")
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return redirect("/")
            return redirect('home')
        else:
            args['login_error'] = "пользователь не найден"
            return render_to_response("Registration/auth.html", args)
    else:
        return render_to_response("Registration/auth.html", args)


def auth_logout(request):
    auth.logout(request)
    return redirect("/")


def reg(request):
    args = {}
    args.update(csrf(request))
    args['form1'] = MyUserForm()
    if request.POST:
        newuser_form = MyUserForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect("/")
        else:
            args['form1'] = newuser_form
    return render_to_response('Registration/registration.html', args)

def account_view(request):
    # если это суперпользователь
    if request.user.is_superuser:
        return redirect('admin')
    # или если это пользователь с галочкой персонал, а так же принадлежащий группе manager
    elif request.user.groups.filter(name='Manager').exists():
        template = 'Registration/homePage.html'
    # или если это пользователь принадлежащий группе manager
    elif request.user.groups.filter(name='Courier').exists():
        template = 'Registration/homePage.html'
    # иначе все остальные (обычные пользователи)
    else:
        template = 'Registration/homePage.html'

    return render(request, template)
