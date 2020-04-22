from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from Market.models import *
from datetime import datetime
from Market.market_forms import ProductForm
from Registration.forms import MyUserForm
from templates import *

def admin(request):
    return render(request, 'admin')


def account_view(request):
    # если это суперпользователь
    if request.user.is_superuser:
        return redirect('admin')
    # или если это пользователь с галочкой персонал, а так же принадлежащий группе manager
    elif request.user.groups.filter(name='Manager').exists():
        # template = 'Market/Manager.html'
        return manager(request)
    # или если это пользователь принадлежащий группе manager
    elif request.user.groups.filter(name='Courier').exists():
        # template = 'Market/Courier.html'
        return courier(request)
    # иначе все остальные (обычные пользователи)
    else:
        return user_page(request)

    return render(request, template)


def manager(request):
    args = {}
    args['reques'] = []
    args['date'] = []
    args['address'] = []
    args['status'] = []
    args['dic'] = []
    # id_status = Request.objects.all().values('id_status')
    my_request = Request.objects.all().filter(id_status__in=[3, 4]).values('id_request', 'date_delivery',
                                                                           'address_delivery', 'id_status')

    for i in my_request:
        args['reques'].append(i.get('id_request'))
        args['date'].append(i.get('date_delivery'))
        args['address'].append(i.get('address_delivery'))
        args['status'].append(i.get('id_status'))
        # args['time_seance'].append(Seance.objects.get(id_seance=i.get('id_seance')).field_time_field)
        # args['row'].append(Seats.objects.get(id_seats=i.get('id_seats')).field_rows_field)
        # args['seat'].append(Seats.objects.get(id_seats=i.get('id_seats')).seats)
        # args['seance'].append(i.get('id_seance'))
        # args['seats'].append(i.get('id_seats'))
    #
    # print(id_seance)
    #
    for i in range(0, len(my_request)):
        if args['status'][i] == 3:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], True])
        elif args['status'][i] == 4:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], False])

    # print(args['dic'])
    print(args)
    return render(request, 'Market/manager.html', {'args': args})


def courier(request):
    args = {}
    args['reques'] = []
    args['date'] = []
    args['address'] = []
    args['status'] = []
    args['dic'] = []
    # id_status = Request.objects.all().values('id_status')
    my_request = Request.objects.all().filter(id_status__in=[3,4], date_delivery=datetime.now()).values('id_request','date_delivery','address_delivery','id_status')

    for i in my_request:
        args['reques'].append(i.get('id_request'))
        args['date'].append(i.get('date_delivery'))
        args['address'].append(i.get('address_delivery'))
        args['status'].append(i.get('id_status'))
        # args['time_seance'].append(Seance.objects.get(id_seance=i.get('id_seance')).field_time_field)
        # args['row'].append(Seats.objects.get(id_seats=i.get('id_seats')).field_rows_field)
        # args['seat'].append(Seats.objects.get(id_seats=i.get('id_seats')).seats)
        # args['seance'].append(i.get('id_seance'))
        # args['seats'].append(i.get('id_seats'))
    #
    # print(id_seance)
    #
    for i in range(0, len(my_request)):
        if args['status'][i]==3:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], True])
        elif args['status'][i]==4:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], False])

    # print(args['dic'])
    print(args)
    return render(request, 'Market/courier.html', {'args': args})

def manager_request(request):
    args = {}
    args['reques'] = []
    args['date'] = []
    args['address'] = []
    args['status_id'] = []
    args['status_name'] = []
    args['dic'] = []
    # id_status = Request.objects.all().values('id_status')
    my_request = Request.objects.all().filter(id_status__in=[1,2,3,4,5,6]).values('id_request', 'date_delivery',
                                                                           'address_delivery', 'id_status')

    for i in my_request:
        args['reques'].append(i.get('id_request'))
        args['date'].append(i.get('date_delivery'))
        args['address'].append(i.get('address_delivery'))
        status = i.get('id_status')
        args['status_id'].append(status)
        status_name = NameRequest.objects.all().filter(id_status=status).values('name_status')
        for j in status_name:
            args['status_name'].append(j.get('name_status'))
        # args['time_seance'].append(Seance.objects.get(id_seance=i.get('id_seance')).field_time_field)
        # args['row'].append(Seats.objects.get(id_seats=i.get('id_seats')).field_rows_field)
        # args['seat'].append(Seats.objects.get(id_seats=i.get('id_seats')).seats)
        # args['seance'].append(i.get('id_seance'))
        # args['seats'].append(i.get('id_seats'))
    #
    # print(id_seance)
    #
    for i in range(0, len(my_request)):
        if args['status_id'][i] in [1,2,3,4]:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], args['status_id'][i], args['status_name'][i],True])
        else:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], args['status_id'][i], args['status_name'][i], False])


# print(args['dic'])
    print(args)
    return render(request, 'Market/Manager_Request.html', {'args': args})

def manager_product(request):
    args = {}
    args['product_id'] = []
    args['category_name'] = []
    args['product_name'] = []
    args['product_quantity'] = []
    args['product_price'] = []
    args['dic'] = []

    args.update(csrf(request))
    args['product_form1'] = ProductForm()
    # if request.POST:
    #     newproduct_form = ProductForm(request.POST)
    #     if newproduct_form.is_valid():
    #         newproduct_form.save()
    #         return redirect("/")
    #     else:
    #         args['product_form1'] = newproduct_form

    my_product = Product.objects.all().values()

    for i in my_product:
        args['product_id'].append(i.get('id_product'))
        # args['category_id'].append(i.get('date_delivery'))
        args['product_name'].append(i.get('name_product'))
        args['product_quantity'].append(i.get('quantity_product'))
        args['product_price'].append(i.get('price_product'))
        category = i.get('id_category_id')
        category_name = NameCategoryProduct.objects.all().filter(id_category=category).values('name_category')
        for j in category_name:
            args['category_name'].append(j.get('name_category'))

    for i in range(0, len(my_product)):
        args['dic'].append([args['product_id'][i], args['category_name'][i], args['product_name'][i], args['product_quantity'][i], args['product_price'][i]])

    # print(args['dic'])
    print(args)
    return render(request, 'Market/Manager_Product.html', {'args': args})

def user_page(request):
    args = {}
    args.update(csrf(request))
    args['form1'] = ProductForm()
    # if request.POST:
    #     newuser_form = ProductForm(request.POST)
    #     if newuser_form.is_valid():
    #         newuser_form.save()
    #         return redirect("/")
    #     else:
    #         args['form1'] = newuser_form
    return render(request, 'Market/User.html', args)


def update_status(request, id_request):
    status = Request.objects.filter(id_request=id_request).values('id_status')
    for i in status:
        st = i.get('id_status')
    Request.objects.filter(id_request=id_request).update(id_status=st + 1)
    return redirect("manager_request")

def down_status(request, id_request):
    Request.objects.filter(id_request=id_request).update(id_status = 6)
    return redirect("manager_request")

def delivery(request, id_request):
    Request.objects.filter(id_request=id_request).update(id_status = 5)
    return redirect("/home/")

def take_delivery(request, id_request):
    Request.objects.filter(id_request=id_request).update(id_status = 4)
    return redirect("/home/")

# def Product_Form(request):
#     args = {}
#     args.update(csrf(request))
#     args['product_form1'] = ProductForm()
#     if request.POST:
#         newproduct_form = ProductForm(request.POST)
#         if newproduct_form.is_valid():
#             newproduct_form.save()
#             return redirect("/")
#         else:
#             args['product_form1'] = newproduct_form
#     return render(request, 'Market/Manager_Product.html', args)
