from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/house_login/")
def post(request):
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
        )
        # user_detail.save()
        # messages.success(request, 'Account created Successfully')
        return redirect('/house_login/')
    return render(request, 'house-signup.html')

def post_success(request):
    return render(request, 'post-success.html')

def product_page(request):
    return render(request, 'product-page.html')

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