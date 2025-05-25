from gc import get_objects
from platform import uname
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import razorpay
# Create your views here.
def index(request):
    return render(request,"index.html")
def signup(request):
    return render(request,"signup.html")
def save_signup(request):
    if request.method=="POST":
        obj = Signup()
        obj.name=request.POST.get("name")
        obj.email=request.POST.get("email")
        obj.mobile=request.POST.get("mobile")
        obj.uname=request.POST.get("uname")
        obj.password=request.POST.get("password")
        obj.save()
        return redirect("/login/")
def Login(request):
    return render(request,"login.html")
def check_log(request):
    uname = request.POST.get("uname")
    password = request.POST.get("password")
    if Signup.objects.filter(uname=uname, password=password).exists():
        u = Signup.objects.get(uname=uname, password=password)
        request.session['user'] = u.id
        return redirect("/user_products/")
    else:
        return redirect("/signup/")
def logout(request):
    return redirect("/")
def admin_log(request):
    return render(request,"admin_log.html")

def check_admin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/Login/")
        else:
            return redirect("/dashboard/")
def dashboard(request):
    return render(request,"dashboard.html")
def country(request):
    a=Country.objects.all()
    return render(request, "country.html", {'a': a})
def add_country(request):
    return render(request,"add_country.html")
def save_country(request):
    if request.method == "POST":
        obj = Country()
        obj.cname = request.POST.get("cname")
        obj.status = request.POST.get("status")
        obj.save()
        return redirect("/country/")
def edit_country(request,id):
    c = Country.objects.get(id=id)
    return render(request, "edit_country.html", {"c": c})
def update_country(request, id):
    obj = Country.objects.get(id=id)
    obj.cname = request.POST.get("cname")
    obj.status = request.POST.get("status")
    obj.save()
    return redirect("/country/")
def delete_country(request,id):
    data = Country.objects.get(id=id)
    data.delete()
    return redirect("/country/")
def add_brand(request):
    return render(request,"add_brand.html")
def save_brand(request):
    if request.method == "POST":
        obj = Brand()
        obj.bimage = request.FILES.get("bimage")
        obj.brand_name = request.POST.get("brand_name")
        obj.brand_status = request.POST.get("brand_status")
        obj.save()
        return redirect("/brand/")
def brand(request):
    b=Brand.objects.all()
    return render(request, "brand.html", {'b':b})
def edit_brand(request,id):
    eb = Brand.objects.get(id=id)
    return render(request, "edit_brand.html", {"eb": eb})
def update_brand(request, id):
    obj = Brand.objects.get(id=id)
    obj.bimage = request.FILES.get("bimage")
    obj.brand_name = request.POST.get("brand_name")
    obj.brand_status = request.POST.get("brand_status")
    obj.save()
    return redirect("/brand/")
def delete_brand(request,id):
    data = Brand.objects.get(id=id)
    data.delete()
    return redirect("/brand/")
def add_category(request):
    return render(request,"add_category.html")
def save_category(request):
    if request.method == "POST":
        obj = Category()
        obj.cimage=request.FILES.get("cimage")
        obj.category_name = request.POST.get("category_name")
        obj.category_status = request.POST.get("category_status")
        obj.save()
        return redirect("/category/")
def category(request):
    c = Category.objects.all()
    return render(request,"category.html",{'c':c})
def edit_category(request,id):
    ec = Category.objects.get(id=id)
    return render(request, "edit_category.html", {"ec": ec})
def update_category(request,id):
    obj = Category.objects.get(id=id)
    obj.cimage = request.FILES.get("cimage")
    obj.category_name = request.POST.get("category_name")
    obj.category_status = request.POST.get("category_status")
    obj.save()
    return redirect("/category/")
def delete_category(request,id):
    data = Category.objects.get(id=id)
    data.delete()
    return redirect("/category/")
def add_product(request):
    return render(request,"add_product.html")
def save_product(request):
    if request.method == "POST":
        obj = Product()
        obj.p_image = request.FILES.get("p_image")
        obj.p_code = request.POST.get("p_code")
        obj.p_name = request.POST.get("p_name")
        obj.p_price = request.POST.get("p_price")
        obj.total_amo = request.POST.get("total_amo")
        obj.p_brand = request.POST.get("p_brand")
        obj.p_category = request.POST.get("p_category")
        obj.p_date= request.POST.get("p_date")
        obj.up_date = request.POST.get("up_date")
        obj.op_stock = request.POST.get("op_stock")
        obj.cp_stock = request.POST.get("cp_stock")
        obj.p_status = request.POST.get("p_status")
        obj.save()
        return redirect("/product/")
def product(request):
    p = Product.objects.all()
    return render(request,"product.html",{'p':p})
def edit_product(request,id):
    ep = Product.objects.get(id=id)
    return render(request,"edit_product.html",{'ep':ep})
def update_product(request,id):
    obj = Product.objects.get(id=id)
    obj.p_image = request.FILES.get("p_image")
    obj.p_code = request.POST.get("p_code")
    obj.p_name = request.POST.get("p_name")
    obj.p_price = request.POST.get("p_price")
    obj.total_amo = request.POST.get("total_amo")
    obj.p_brand = request.POST.get("p_brand")
    obj.p_category = request.POST.get("p_category")
    obj.p_date = request.POST.get("p_date")
    obj.up_date = request.POST.get("up_date")
    obj.op_stock = request.POST.get("op_stock")
    obj.cp_stock = request.POST.get("cp_stock")
    obj.p_status = request.POST.get("p_status")
    obj.save()
    return redirect("/product/")
def delete_product(request,id):
    data = Product.objects.get(id=id)
    data.delete()
    return redirect("/product/")
def user_products(request):
    up = Product.objects.only('p_image','p_code','p_name', 'total_amo', 'p_brand','p_category','p_date','up_date','p_status')
    return render(request,"user_products.html",{'up':up})
    # ✅ Ensures only logged-in users can add to cart
def add_to_cart(request, id):
    if 'user' in request.session:
        user_id = request.session['user']
        user = Signup.objects.get(id=user_id)
        product = Product.objects.get(id=id)

        cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect("/cart/")
    else:
        return redirect("/login/")


def cart(request):
    if 'user' not in request.session:
        return redirect("/login/")
    user_id = request.session['user']
    user = Signup.objects.get(id=user_id)

    if request.method == "POST":
        item_id = request.POST.get("item_id")
        action = request.POST.get("action")

        if action in ["increase", "decrease", "remove"]:
            cart_item = Cart.objects.get(id=item_id)

            if action == "increase":
                cart_item.quantity += 1
                cart_item.save()
            elif action == "decrease":
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
                else:
                    cart_item.delete()
            elif action == "remove":
                cart_item.delete()

    cart_items = Cart.objects.filter(user=user)
    updated_items = []
    total_amount = 0

    for item in cart_items:
        item_total = item.quantity * item.product.p_price
        total_amount += item_total
        updated_items.append({
            'id': item.id,
            'product': item.product,
            'quantity': item.quantity,
            'item_total': item_total,
        })

    request.session['total_amount'] = total_amount

    return render(request, 'cart.html', {'cart_items': updated_items, 'total_amount': total_amount})


def checkout(request):
    razorpay_client = razorpay.Client(auth=('rzp_test_9zruMnoLDlsCLG', 'oXUZ9Mf5zhjoZsTFLc7RpABO'))
    total_amount = request.session.get('total_amount')
    if total_amount is None:
        return redirect('/cart/')
    amount = int(total_amount * 100)
    currency = 'INR'
    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': 'rzp_test_9zruMnoLDlsCLG',  # Corrected merchant key
        'razorpay_amount': amount,
        'currency': currency
    }
    return render(request, 'checkout.html',context)


def save_order(request):
    if request.method == 'POST':
        obj = Order()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phn_no = request.POST.get('phn_no')
        obj.address = request.POST.get('address')
        obj.payment_method = request.POST.get('payment_method')
        obj.order_id = request.POST.get('order_id')
        obj.payment_id = request.POST.get('payment_id')
        cart_items = Cart.objects.filter(user_id=request.session['user'])
        products = ''
        for item in cart_items:
            products += str(item.product.p_name) + ', '
        obj.products = products
        obj.save()
        return render(request,'user_products.html')
#def oder_details(request):
#    o = Order.objects.filter(status='pending')
  #  return render(request,'oder_details.html',{'o': o})
def oder_details(request):
    o = Order.objects.filter(status='pending')
    return render(request,'oder_details.html',{'o':o})
def oder_details(request):
    o = Order.objects.filter(status='pending')
    return render(request,'oder_details.html',{'o': o})
def add_delivery_p(request):
    return render(request,"add_delivery_p.html")
def save_delivery(request):
    if request.method == 'POST':
        obj = Deliveryp()
        obj.dp_id = request.POST.get('dp_id')
        obj.dp_pic = request.FILES.get("dp_pic")
        obj.dp_name = request.POST.get('dp_name')
        obj.dp_email = request.POST.get('dp_email')
        obj.dp_number = request.POST.get('dp_number')
        obj.dp_uname = request.POST.get('dp_uname')
        obj.dp_password = request.POST.get('dp_password')
        obj.dp_date = request.POST.get('dp_date')
        obj.save()
        return redirect("/delivery_p/")
def delivery_p(request):
    dp=Deliveryp.objects.all()
    return render(request,"delivery_p.html",{'dp':dp})
def edit_dpartner(request,id):
    edp = Deliveryp.objects.get(id=id)
    return render(request,"edit_dpartner.html",{'edp':edp})
def update_dpartner(request,id):
    obj = Deliveryp.objects.get(id=id)
    obj.dp_id = request.POST.get("dp_id")
    obj.dp_pic = request.FILES.get("dp_pic")
    obj.dp_name = request.POST.get("dp_name")
    obj.dp_email = request.POST.get("dp_email")
    obj.dp_number = request.POST.get("dp_number")
    obj.dp_uname = request.POST.get("dp_uname")
    obj.dp_password = request.POST.get("dp_password")
    obj.dp_date = request.POST.get("dp_date")
    obj.save()
    return redirect("/delivery_p/")
def delete_dpartner(request,id):
    x = Deliveryp.objects.get(id=id)
    x.delete()
    return redirect("/delivery_p/")



def out_delivery(request, id):
    od = Deliveryp.objects.values_list('dp_name', flat=True)
    order_obj = Order.objects.get(id=id)
    if request.method == 'POST':
        delivery_partner = request.POST.get('delivery_partner')
        delivery_partner_obj = Deliveryp.objects.get(dp_name=delivery_partner)
        Oder_notification.objects.create(
            dp_name=delivery_partner_obj,
            order_id=order_obj,
            message=f'New order assigned: Order ID {order_obj.id}, Product: {order_obj.products}, Customer Name: {order_obj.name}, Address: {order_obj.address}, Phone: {order_obj.phn_no}'
        )
        delivery_partner_email = delivery_partner_obj.dp_email
        send_mail(
            'New Order Assignment',
            f'Dear {delivery_partner},\n\nYou have been assigned a new order.',
            settings.EMAIL_HOST_USER,
            [delivery_partner_email],
            fail_silently=False,
        )
        order_obj.status = 'out_for_delivery'
        order_obj.save()
        return redirect('/oder_details/')
    return render(request, "out_delivery.html", {'od': od, 'order':order_obj})

def deli_home(request):
    return render(request,"deli_home.html")
def dp_login(request):
    return render(request,"dp_login.html")
def check_dp_login(request):
    if request.method == 'POST':
        dname = request.POST.get("d_name")
        password = request.POST.get("password")
        if Deliveryp.objects.filter(dp_uname=dname, dp_password=password).exists():
            p = Deliveryp.objects.get(dp_uname=dname, dp_password=password)
            request.session['user'] = p.dp_uname
            return redirect("/d_notifications/")
        else:
            return render(request, "dp_login")
    return render(request, "dp_login")

#def d_notifications(request):
  #  dp_name = request.session['user']
  #  delivery_partner = Deliveryp.objects.get(dp_uname=dp_name)
  #  notifications = Oder_notification.objects.filter(dp_name=delivery_partner)
   # if request.method == 'POST':
       # for notification in notifications:
           # action = request.POST.get(f'r{notification.id}')
           # if action == 'accept':
                # Update notification status
               # notification.status = 'accepted'
               # notification.save()
                # Update order status
               # order = notification.order_id
               # order.status = 'accepted'
               # order.save()
           # elif action == 'reject':
                # Update notification status
                #notification.status = 'rejected'
                #notification.save()
                #order = notification.order_id
               # order.status = 'rejected'
               # order.save()
        #return redirect('/d_notifications/')
   # return render(request, 'd_notifications.html', {'notifications': notifications})
def d_notifications(request):
    dp_name = request.session['user']
    delivery_partner = Deliveryp.objects.get(dp_uname=dp_name)
    notifications = Oder_notification.objects.filter(dp_name=delivery_partner)
    if request.method == 'POST':
        for notification in notifications:
            action = request.POST.get(f'r{notification.id}')
            if action == 'accept':
                notification.status = 'accepted'
                notification.save()
                order = notification.order_id
                order.status = 'accepted'
                order.save()
            elif action == 'reject':
                notification.status = 'rejected'
                notification.save()
                order = notification.order_id
                order.status = 'pending'
                order.save()
        return redirect('/d_notifications/')
    return render(request, 'd_notifications.html', {'notifications': notifications})


def d_logout(request):
    return redirect("/")
def completed_orders(request):
    notifications = Oder_notification.objects.filter(status='accepted')
    completed_orders = {}
    for n in notifications:
        if n.order_id.id not in completed_orders:
            completed_orders[n.order_id.id] = {
                'order': n.order_id,
                'delivery_partners': [n.dp_name.dp_name]
            }
        else:
            completed_orders[n.order_id.id]['delivery_partners'].append(n.dp_name.dp_name)
    return render(request, 'completed_orders.html', {'completed_orders': completed_orders.values()})
def enquiry(request):
    return render(request,"enquiry.html")
def save_enq(request):
    if request.method=="POST":
        obj = Enquiry()
        obj.e_name=request.POST.get("e_name")
        obj.e_email = request.POST.get("e_email")
        obj.e_phone = request.POST.get("e_phone")
        obj.e_question = request.POST.get("e_question")
        obj.save()
        return redirect('/enquiry/')
def enquires(request):
    eq=Enquiry.objects.all()
    return render(request,"enquires.html",{'eq':eq})
def my_orders(request):
    user_id = request.session['user']
    user = Signup.objects.get(id=user_id)
    orders = Order.objects.filter(name=user.name, status='accepted')
    order_products = []
    for order in orders:
        product_names = order.products.split(', ')
        products = Product.objects.filter(p_name__in=product_names)
        for product in products:
            order_products.append({
                'order_id': order.id,
                'product_name': product.p_name,
                'product_image': product.p_image,
                'price': product.p_price,
                'brand': product.p_brand,
                'category': product.p_category
            })
    return render(request, 'my_orders.html', {'order_products': order_products})











