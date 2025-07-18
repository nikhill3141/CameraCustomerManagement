from django.shortcuts import render,redirect, get_object_or_404
from .models import Customer

from django.db.models import Q
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User


# Create your views here.

def landing_page(request):
  return render(request,'landing_page.html')

def add(request):
  return render(request,'add.html')

def search(request):
  return render(request,'search.html')

def add_customer(request):
  if request.method == 'POST':
    fullName = request.POST.get('full_name')
    mobileNumber = request.POST.get('mobile_number')
    address = request.POST.get('address')
    orderType = request.POST.get('order_type')
    orderDescription = request.POST.get('order_description')
    totalPrice = request.POST.get('total_price')
    paidPrice = request.POST.get('paid_price')
    
    Customer.objects.create(
      user_id = request.user.id,
      full_name = fullName,
      mobile_no = mobileNumber,
      address = address,
      order_type = orderType,
      order_description = orderDescription,
      total_price = totalPrice,
      paid_price = paidPrice
    )
    return redirect('dashboard')
  return render(request,'customer/add_customer.html')


# def display_customer_dashboard(request):
#   customers = Customer.objects.all()
#   return render(request,'dashboard.html',{"customers":customers})

# all customer query 
def customer_list(request):
  customers = Customer.objects.filter(user_id=request.user.id)

  query = request.GET.get('q','')
  if query:
    customers = customers.filter(Q(full_name__icontains=query) | Q(mobile_no__icontains=query))
  return render(request,'customer/all_customer.html',{"customers":customers})


# login
def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)

    if user:
      login(request,user)
      return redirect('dashboard')
  return render(request,'login.html')

def user_logout(request):
  logout(request)
  return redirect('landing_page')

def signup_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    user = User.objects.create(
      username=username,
      email=email
    )
    user.set_password(password),
    user.save()
    login(request,user)
    return redirect('dashboard')
  return render(request,'signup.html')



def customer_edit(request, id):
  customer = Customer.objects.filter(id=id).first()

  if request.method == 'POST':
    fullName = request.POST.get('full_name')
    mobileNumber = request.POST.get('mobile_number')
    address = request.POST.get('address')
    orderType = request.POST.get('order_type')
    orderDescription = request.POST.get('order_description')
    totalPrice = request.POST.get('total_price')
    paidPrice = request.POST.get('paid_price')

    
    customer.full_name = fullName
    customer.mobile_no = mobileNumber
    customer.address = address
    customer.order_type = orderType
    customer.order_description = orderDescription
    customer.total_price = float(totalPrice)
    customer.paid_price = float(paidPrice)
    customer.save()
    return redirect('all_customer')
  return render(request,'customer/edit_customer.html', {"customer":customer})

def delete_customer(id):
  customer = Customer.objects.filter(id=id).filter()
  customer.delete()
  return  redirect('all_customer')