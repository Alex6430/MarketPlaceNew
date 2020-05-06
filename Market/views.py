from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from Market.models import *
from datetime import datetime
from Market.market_forms import *
from Registration.forms import MyUserForm
from templates import *
from Registration.views import index
from datetime import *

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
    elif request.user.username:
        # template = 'Market/Courier.html' AnonymousUser
        return index(request)
    # иначе все остальные (обычные пользователи)
    else:
        return index(request)

    return render(request, 'Registration/homePage.html')


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
    args['product_form1'] = UpdateProductForm()
    args['create_product_form1'] = CreateProductForm()
    args['create_category_product_form1'] = NameCategoryForm()

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
    # args.update(csrf(request))
    # args['form1'] = ProductForm()
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

def down_status_user(request, id_request):
    Request.objects.filter(id_request=id_request).update(id_status = 6)
    return redirect("user_request")

def delivery(request, id_request):
    Request.objects.filter(id_request=id_request).update(id_status = 5)
    return redirect("/home/")

def take_delivery(request, id_request):
    Request.objects.filter(id_request=id_request).update(id_status = 4)
    return redirect("/home/")

def update_product(request,product_id):
    try:
        product = Product.objects.get(id_product=product_id)
        if request.POST:
            newproduct_form = UpdateProductForm(request.POST)
            if newproduct_form.is_valid():
                # product.id_category = newproduct_form.cleaned_data['id_category']
                product.name_product = newproduct_form.cleaned_data['name_product']
                product.quantity_product = newproduct_form.cleaned_data['quantity_product']
                product.price_product = newproduct_form.cleaned_data['price_product']
                product.save()
                return redirect("manager_product")
            # else:
                # args['product_form1'] = newproduct_form
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

    return manager_product(request)

def create_product(request):

    try:
        create_product = Product()
        if request.POST:
            newcreateproduct_form = CreateProductForm(request.POST)
            category_product_form = NameCategoryForm(request.POST)
            if newcreateproduct_form.is_valid() and category_product_form.is_valid():
                create_product.name_product = newcreateproduct_form.cleaned_data['name_product']
                create_product.quantity_product = newcreateproduct_form.cleaned_data['quantity_product']
                create_product.price_product = newcreateproduct_form.cleaned_data['price_product']
                category = category_product_form.cleaned_data['name_category']
                new_id_category = NameCategoryProduct.objects.filter(name_category=category).values('id_category')
                if new_id_category:
                    for i in new_id_category:
                        pr = i.get('id_category')
                        create_product.id_category_id = pr
                else:
                    NCP = NameCategoryProduct()
                    NCP.name_category = category
                    NCP.save()
                    new_id_category = NameCategoryProduct.objects.filter(name_category=category).values('id_category')
                    for i in new_id_category:
                        create_product.id_category_id = i.get('id_category')

                create_product.save()
                return redirect("manager_product")
            # else:
            #     args['create_product_form1'] = newcreateproduct_form
                # args['create_product_form1'] = newcreateproduct_form
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

    return manager_product(request)

def bay(request, product_id, id_user):
    print(product_id,id_user)
    my_Request = Request.objects.all().filter(id_user=id_user,id_status=1).values()
    price = Product.objects.get(id_product=product_id).price_product
    if my_Request.exists():
        print('not empty')
        status = Request.objects.get(id_user=id_user,id_status=1).id_request
        myProductRequest = ProductRequest.objects.all().filter(id_product_id=product_id, id_request_id=status).values()
        if myProductRequest.exists():
            qantity = ProductRequest.objects.get(id_product_id=product_id, id_request_id=status).quantity
            new_product_request = ProductRequest(id_product_id=product_id, id_request_id=status, quantity=qantity+1)
            new_product_request.save()
            old_price = Request.objects.get(id_user=id_user,id_status=1).price_request
            new_request = Request(id_request=status, id_user_id=id_user, id_status_id=1, price_request=old_price+price, date_delivery=datetime.now(),
                                  address_delivery="ghd")
            new_request.save()
        else:
            new_product_request = ProductRequest(id_product_id=product_id, id_request_id=status, quantity=1)
            new_product_request.save()
            old_price = Request.objects.get(id_user=id_user,id_status=1).price_request
            new_request = Request(id_request=status, id_user_id=id_user, id_status_id=1, price_request=old_price + price,
                                  date_delivery=datetime.now(),
                                  address_delivery="ghd")
            new_request.save()
    else:
        print("empty")
        new_request = Request(id_user_id=id_user,id_status_id=1,price_request=price,date_delivery=datetime.now(),address_delivery="ghd")
        new_request.save()
        status = Request.objects.get(id_user=id_user,id_status=1).id_request
        new_product_request = ProductRequest(id_product_id=product_id,id_request_id=status,quantity=1)
        new_product_request.save()

    return index(request)

def car_page_with_product(request, category_id):
    args = {}
    args['product_id'] = []
    args['product_name'] = []
    args['product_quantity'] = []
    args['product_price'] = []
    args['category_name'] = []
    args['dic'] = []

    name_categ = NameCategoryProduct.objects.all().filter(id_category=category_id).values()
    # id_categor = NameCategoryProduct.objects.all().filter(name_category='шины').values('id_category')
    my_product = Product.objects.all().filter(id_category=category_id).values()

    for i in name_categ:
        args['category_name'].append(i.get('name_category'))

    for i in my_product:
        args['product_id'].append(i.get('id_product'))
        # args['category_id'].append(i.get('date_delivery'))
        args['product_name'].append(i.get('name_product'))
        args['product_quantity'].append(i.get('quantity_product'))
        args['product_price'].append(i.get('price_product'))

    for i in range(0, len(my_product)):
        args['dic'].append(
            [args['product_id'][i], args['product_name'][i], args['product_quantity'][i],
             args['product_price'][i]])

    return render(request, 'Market/Page_With_Product/carPageWithProduct.html', {'args': args})

def bin(request, id_user):
    args = {}
    args['request_id'] = []
    args['product_name'] = []
    args['product_quantity'] = []
    args['product_price'] = []
    args['request_price'] = []
    # args['category_name'] = []
    args['dic'] = []

    args.update(csrf(request))
    args['request_form1'] = UpdateRequestForm()


    my_Request = Request.objects.all().filter(id_user=id_user, id_status=1).values()
    # request_id = Request.objects.get(id_user=id_user, id_status=1).id_request
    # pr_req = ProductRequest.objects.all().filter(id_request=request_id).values()



    for i in my_Request:
        args['request_id'].append(i.get('id_request'))
        pr_req = ProductRequest.objects.all().filter(id_request=i.get('id_request')).values()
        for j in pr_req:
            pr_id = Product.objects.all().filter(id_product=j.get('id_product_id')).values()
            for k in pr_id:
                args['product_name'].append(k.get('name_product'))
                args['product_price'].append(k.get('price_product'))
            args['product_quantity'].append(j.get('quantity'))
        args['request_price'].append(i.get('price_request'))

    if my_Request.exists():
        for i in range(0, len(pr_req)):
            args['dic'].append(
                [args['product_name'][i], args['product_quantity'][i],args['product_quantity'][i]*args['product_price'][i]])

    return render(request, 'Market/bin.html', {'args': args})

def update_request(request,id_request):
    request_id=id_request
    try:
        newrequest = Request.objects.get(id_request=request_id)
        if request.POST:
            newrequest_form = UpdateRequestForm(request.POST)
            if newrequest_form.is_valid():
                # product.id_category = newproduct_form.cleaned_data['id_category']
                newrequest.address_delivery = newrequest_form.cleaned_data['address_delivery']
                newrequest.date_delivery = newrequest_form.cleaned_data['date_delivery']
                newrequest.id_status_id = 2
                newrequest.save()
                return redirect("index")
            # else:
                # args['product_form1'] = newproduct_form
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

    return index(request)


def user_request(request, id_user):
    args = {}
    args['reques'] = []
    args['date'] = []
    args['address'] = []
    args['status_id'] = []
    args['status_name'] = []
    args['dic'] = []
    # id_status = Request.objects.all().values('id_status')
    my_request = Request.objects.all().filter(id_status__in=[1,2,3,4,5,6], id_user=id_user).values('id_request', 'date_delivery',
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
        if args['status_id'][i] in [1,2,3]:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], args['status_id'][i], args['status_name'][i],True])
        else:
            args['dic'].append([args['reques'][i], args['date'][i], args['address'][i], args['status_id'][i], args['status_name'][i], False])


# print(args['dic'])
    print(args)
    return render(request, 'Market/User_Request.html', {'args': args})

