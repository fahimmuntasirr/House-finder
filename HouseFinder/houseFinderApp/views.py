from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    queryset = user_details.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(require__icontains = request.GET.get('search'))
        # queryset = queryset.filter(product_address__icontains = request.GET.get('search2'))
    context = {'queryset' : queryset}
    return render(request, 'index.html', context)

@login_required(login_url="/house_login/")
def post(request):
    if request.method == 'POST':
        product_contact = request.POST.get('product_contact')
        product_address = request.POST.get('product_address')
        product_price = request.POST.get('product_price')
        product_description = request.POST.get('product_description')
        username = request.POST.get('username')
        require = request.POST.get('require')
        # date = request.POST.get('date')
        product_pic = request.FILES.get('product_pic')
        # product_address = request.POST.get('product_address')
        product_title = request.POST.get('product_title')

        user1 = User.objects.filter(username=username).first()

        user_detail = user_details.objects.get(user = user1)
        if product_contact:
            user_detail.product_contact = product_contact
        if product_pic:
            user_detail.product_pic = product_pic
        if product_price:
            user_detail.product_price = product_price
        if require:
            user_detail.require = require
        user_detail.product_address = product_address
        user_detail.product_title = product_title
        user_detail.product_description = product_description
        user_detail.if_posted = 1
        user_detail.save()
        return redirect('/post_success/')
    return render(request, 'post.html')

def house_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/house_login/')
        
        user = authenticate( username = username, password = password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/house_login/')

        else:
            login(request,user)
            print(user.first_name)
            return redirect('/')
    return render(request, 'house-login.html')

def house_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        dp= request.FILES.get('dp')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/house_signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        user_details.objects.create(
            user = user,
            dp = dp,
            date = date,
            gender = gender,
            address = address,
            if_posted = 0,
        )
        # user_detail.save()
        # messages.success(request, 'Account created Successfully')
        return redirect('/house_login/')
    return render(request, 'house-signup.html')

def post_success(request):
    return render(request, 'post-success.html')

def product_page(request,id):
    product = user_details.objects.get(id=id)
    context = {'product' : product}
    return render(request, 'product-page.html', context)

@login_required(login_url="/house_login/")
def profile1(request,id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # profile_dp= request.FILES.get('profile_dp')
        date = request.POST.get('date')
        dp = request.FILES.get('dp')
        address = request.POST.get('address')
        description = request.POST.get('description')

        user = User.objects.get(username = id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user1 = User.objects.filter(username=id).first()
        user_detail = user_details.objects.get(user = user1)
        user_detail.date = date
        if dp:
            user_detail.dp = dp
        user_detail.address = address
        user_detail.description = description
        user_detail.save()
        return redirect('/')
    return render(request, 'profile1.html')

def logout_page(request):
    logout(request)
    return redirect('/')