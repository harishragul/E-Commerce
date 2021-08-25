from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as dj_login, logout
from .forms import CreateUserForm, CustomerForm, RequireForm, DealerForm, ProductForm, PackForm, ShipForm, ShipStatusForm, ShipStatusForm2, ShipStatusForm3
import json
from .models import *
import datetime
from django.contrib import messages

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        customer = 'Login'
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'customer': customer, 'categorys': categorys}
    return render(request, 'store/store.html', context)

def require(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        customer = 'Login'
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    form = RequireForm(initial={'customer': request.user.customer})
    if request.method == "POST":
        form = RequireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('require')
        else:
            print("Invalid")

    requires = Require.objects.all()
    categorys = Category.objects.all()
    context = {'form':form, 'requires':requires, 'cartItems': cartItems, 'customer': str(customer), 'categorys': categorys}
    return render(request, 'store/require.html', context)

def delete_require(request, require_id):
    context ={}

    obj = Require.objects.get(pk=require_id)

    if request.method =="POST":
        obj.delete()
        return redirect('require')

    return render(request, "store/require_delete.html", context)

def product(request, product_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    product = Product.objects.get(pk=product_id)
    categorys = Category.objects.all()

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'product': product, 'categorys': categorys, 'customer': customer,}
    return render(request, 'store/product.html', context)

def dealer_product(request):
    if request.user.is_authenticated:
        customer = request.user.shop
        print(customer)
    else:
        return redirect('dealer_login')

    form = ProductForm(initial={'shop': request.user.shop})
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dealer_product')
        else:
            print("Invalid")

    products = Product.objects.all()
    context = {'form':form, 'products': products, 'shop':customer}
    return render(request, 'store/dealer_product.html', context)

def ship_home(request):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    items = OrderItem.objects.all()
    ships = ShippingAddress.objects.all()

    context = {'items':items, 'customer': customer, 'ships': ships}
    return render(request, 'store/ship_home.html', context)

def shipped(request):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    items = OrderItem.objects.all()
    ships = ShippingAddress.objects.all()

    context = {'items':items, 'customer': customer, 'ships': ships}
    return render(request, 'store/shipped.html', context)

def dealer_home(request):
    if request.user.is_authenticated:
        customer = request.user.shop
        print(customer)
    else:
        return redirect('dealer_login')

    items = OrderItem.objects.all()
    ships = ShippingAddress.objects.all()

    context = {'items':items, 'customer': customer, 'ships': ships}
    return render(request, 'store/dealer_home.html', context)

def delivery(request):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    items = OrderItem.objects.all()
    ships = ShippingAddress.objects.all()

    context = {'items':items, 'customer': customer, 'ships': ships}
    return render(request, 'store/delivery.html', context)

def out_for(request):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    items = OrderItem.objects.all()
    ships = ShippingAddress.objects.all()

    context = {'items':items, 'customer': customer, 'ships': ships}
    return render(request, 'store/out_for.html', context)

def order_placed(request, orderItem_id):
    if request.user.is_authenticated:
        customer = request.user.shop
        print(customer)
    else:
        return redirect('dealer_login')

    form = PackForm(instance=OrderItem.objects.get(pk=orderItem_id))
    if request.method == "POST":
        form = PackForm(request.POST, instance=OrderItem.objects.get(pk=orderItem_id))
        if form.is_valid():
            form.save()
            return redirect('dealer_home')
        else:
            print("Invalid")

    product = OrderItem.objects.get(pk=orderItem_id)
    ships = ShippingAddress.objects.all()
    context = {'product':product, 'customer':customer,'ships':ships, 'form':form}

    return render(request, 'store/order_placed.html', context)

def ship_home_product(request, ship_home_product_id):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    form = ShipStatusForm(instance=OrderItem.objects.get(pk=ship_home_product_id))
    if request.method == "POST":
        form = ShipStatusForm(request.POST, instance=OrderItem.objects.get(pk=ship_home_product_id))
        if form.is_valid():
            form.save()
            return redirect('ship_home')
        else:
            print("Invalid")

    item = OrderItem.objects.get(pk=ship_home_product_id)
    ships = ShippingAddress.objects.all()

    context = {'item':item, 'customer': customer, 'ships': ships, 'form':form}
    return render(request, 'store/ship_home_product.html', context)

def shipped_product(request, shipped_product_id):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    form = ShipStatusForm2(instance=OrderItem.objects.get(pk=shipped_product_id))
    if request.method == "POST":
        form = ShipStatusForm2(request.POST, instance=OrderItem.objects.get(pk=shipped_product_id))
        if form.is_valid():
            form.save()
            return redirect('ship_home')
        else:
            print("Invalid")

    item = OrderItem.objects.get(pk=shipped_product_id)
    ships = ShippingAddress.objects.all()

    context = {'item':item, 'customer': customer, 'ships': ships, 'form':form}
    return render(request, 'store/shipped_product.html', context)

def out_for_product(request, out_for_product_id):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    form = ShipStatusForm3(instance=OrderItem.objects.get(pk=out_for_product_id))
    if request.method == "POST":
        form = ShipStatusForm3(request.POST, instance=OrderItem.objects.get(pk=out_for_product_id))
        if form.is_valid():
            form.save()
            return redirect('ship_home')
        else:
            print("Invalid")

    item = OrderItem.objects.get(pk=out_for_product_id)
    ships = ShippingAddress.objects.all()

    context = {'item':item, 'customer': customer, 'ships': ships, 'form':form}
    return render(request, 'store/out_for_product.html', context)

def delivery_product(request, delivery_product_id):
    if request.user.is_authenticated:
        customer = request.user.ship
        print(customer)
    else:
        return redirect('ship_login')

    item = OrderItem.objects.get(pk=delivery_product_id)
    ships = ShippingAddress.objects.all()

    context = {'item':item, 'customer': customer, 'ships': ships}
    return render(request, 'store/delivery_product.html', context)

def order_detail(request, orderItem_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    product = OrderItem.objects.get(pk=orderItem_id)
    ships = ShippingAddress.objects.all()
    categorys = Category.objects.all()
    context = {'product':product, 'customer':customer, 'cartItems': cartItems,'ships':ships, 'categorys': categorys,}

    return render(request, 'store/order_detail.html', context)

def search(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        customer = 'Login'
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    search = request.GET['query']
    products = Product.objects.filter(name__icontains=search)
    categorys = Category.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'customer': customer, 'categorys': categorys, 'search': search}
    return render(request, 'store/search.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    categorys = Category.objects.all()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'customer': customer, 'categorys': categorys}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    categorys = Category.objects.all()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'categorys': categorys, 'customer': customer,}
    return render(request, 'store/checkout.html', context)

def dealer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                dj_login(request, user)
                shop = str(request.user.shop)
                print(shop)
                if 'None' in shop:
                    return redirect('dealer_info')
                else:
                    return redirect('dealer_home')
            except:
                messages.info(request, 'Username or password is invalid')

        else:
            messages.info(request, 'Username or password is invalid')

    context = {}
    return render(request, 'store/dealer_login.html', context)

def ship_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                dj_login(request, user)
                ship = str(request.user.ship)
                print(ship)
                if 'None' in ship:
                    return redirect('ship_info')
                else:
                    return redirect('ship_home')
            except:
                messages.info(request, 'Username or password is invalid')

        else:
            messages.info(request, 'Username or password is invalid')

    context = {}
    return render(request, 'store/ship_login.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                dj_login(request, user)
                customer = str(request.user.customer)
                print(customer)
                if 'None' in customer:
                    return redirect('info')
                else:
                    return redirect('store')
            except:
                messages.info(request, 'Username or password is invalid')

        else:
            messages.info(request, 'Username or password is invalid')

    context = {}
    return render(request, 'store/login.html', context)

def logoutsite(request):
    logout(request)
    return redirect('login')

def dealer_logoutsite(request):
    logout(request)
    return redirect('dealer_login')

def ship_logoutsite(request):
    logout(request)
    return redirect('ship_login')

def dealer_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Shop.objects.create(user=user)
            return redirect('dealer_login')

        else:
            messages.info(request, 'Try Again(Either Username not unique or Password mismatch).')

    context = {'form':form}
    return render(request, 'store/dealer_register.html', context)

def ship_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Ship.objects.create(user=user)
            return redirect('ship_login')

        else:
            messages.info(request, 'Try Again(Either Username not unique or Password mismatch).')

    context = {'form':form}
    return render(request, 'store/ship_register.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user)
            return redirect('login')

        else:
            messages.info(request, 'Try Again(Either Username not unique or Password mismatch).')

    context = {'form':form}
    return render(request, 'store/register.html', context)

def info(request):
    form =  CustomerForm(instance=Customer.objects.get(user=request.user))
    if request.method == 'POST':
        print(request.POST)
        form =  CustomerForm(request.POST, instance=Customer.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('store')
        else:
            print("invalid Form")

    context = {'form':form}
    return render(request, 'store/info.html', context)

def dealer_info(request):
    form =  DealerForm(instance=Shop.objects.get(user=request.user))
    if request.method == 'POST':
        form =  DealerForm(request.POST, instance=Shop.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('dealer_home')
        else:
            print("invalid Form")

    context = {'form':form}
    return render(request, 'store/dealer_info.html', context)

def ship_info(request):
    form =  ShipForm(instance=Ship.objects.get(user=request.user))
    if request.method == 'POST':
        form =  ShipForm(request.POST, instance=Ship.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('ship_home')
        else:
            print("invalid Form")

    context = {'form':form}
    return render(request, 'store/ship_info.html', context)

def profile(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    customer = Customer.objects.get(user=request.user)
    things = OrderItem.objects.all()
    categorys = Category.objects.all()
    ships = ShippingAddress.objects.all()
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'categorys': categorys, 'things': things, 'customer': customer, 'ships': ships}
    return render(request, 'store/profile.html', context)

def category(request, category_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        customer = 'Login'
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    category = Category.objects.get(pk=category_id)
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'customer': customer, 'categorys': categorys, 'category': category}
    return render(request, 'store/category.html', context)

def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        customer = 'Login'
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    products = Product.objects.all()
    categorys = Category.objects.all()
    shops = Shop.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'customer': customer, 'categorys': categorys, 'shops': shops}
    return render(request, 'store/shop.html', context)

def entity(request, entity_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        customer = 'Login'
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' : False}
        cartItems = order['get_cart_items']
        return redirect('login')

    products = Product.objects.all()
    categorys = Category.objects.all()
    shops = Shop.objects.all()
    shop = Shop.objects.get(pk=entity_id)
    context = {'products': products, 'cartItems': cartItems, 'customer': customer, 'categorys': categorys, 'shops': shops, 'shop': shop}
    return render(request, 'store/entity.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
            name = data['form']['name'],
            number = data['form']['number'],
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in')

    return JsonResponse('Payment Submited', safe=False)
