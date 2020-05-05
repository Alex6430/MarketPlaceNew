from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from Registration.forms import MyUserForm
from Market.models import *



def admin(request):
    return render(request, 'admin')

def index(request):
    args = {}
    args['category_id'] = []
    args['category_name'] = []
    args['main_category'] = []
    args['other_category'] = []
    main_category = ['шины','диски','масла','аккумуляторы']
    other_category = ['шины', 'диски', 'масла', 'аккумуляторы']

    my_main_category = NameCategoryProduct.objects.all().filter(name_category__in=main_category).values()
    my_other_category = NameCategoryProduct.objects.all().exclude(name_category__in=main_category).values()

    for i in my_main_category:
        args['category_id'].append(i.get('id_category'))
        args['category_name'].append(i.get('name_category'))

    for i in range(0, len(my_main_category)):
        args['main_category'].append(
            [args['category_id'][i], args['category_name'][i]])

    args['category_id'] = []
    args['category_name'] = []
    for i in my_other_category:
        args['category_id'].append(i.get('id_category'))
        args['category_name'].append(i.get('name_category'))

    for i in range(0, len(my_other_category)):
        args['other_category'].append(
            [args['category_id'][i], args['category_name'][i]])


    return render(request, 'Registration/homePage.html', {'args': args})

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
            return redirect("home")
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
