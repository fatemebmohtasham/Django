from django.shortcuts import render,redirect
from . models import Product,Customer,Order,User
from . forms import OrderForm,UserForm,CustomerForm,ProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models  import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from.decorator import admin_only,allowed_user



def login_page(request):
  if request.method =='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    try:
       user=User.objects.get(username=username)
    except:
       messages.error(request,'user does not exist')

    user=authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user) 
      return redirect('dashboard')
    else:
      messages.error(request,'username or password is not correct')       
  return render(request,'account/login.html')

def user_register(request):
	form=UserForm()
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			user.save()
      
			group=Group.objects.get(name='customer')
			user.groups.add(group)
			Customer.objects.create(
				user=user,
				name=user.name,
				phone=user.phone,
				email=user.email,
			)

			messages.success(request,'account was created')
			return redirect('login')
	context={'forms':form}
	return render(request,'account/register.html',context)		




def logout_page(request):
  logout(request)
  return redirect('dashboard')


def dashboard(request):
	customers=Customer.objects.all()
	orders=Order.objects.exclude(product__isnull=True)
	total_customers=customers.count()
	total_orders=orders.count()
	delivere=Order.objects.filter(status='Delivered').count()
	pending=Order.objects.filter(status='Pending').count()
	context={'customers': customers,'total_customers':total_customers,
	'orders':orders,'total_orders':total_orders,'delivered':delivere,
	'pending':pending}
	return render (request,'account/dashboard.html',context)

@allowed_user(allowed_roles=['admin'])
@admin_only
def product(request):
	product=Product.objects.all()
	context={'products':product}
	return render (request,'account/products.html',context)

@allowed_user(allowed_roles=['admin'])
@admin_only
def create_product(request):
	form=ProductForm
	if request.method == 'POST':
		form=ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('products')
	context={'forms':form,}
	return render (request,'account/product_form.html',context)

@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_product(request,pk):
	product=Product.objects.get(id=pk)
	if request.method == 'POST':
		product.delete()
		return redirect ('products')
	return render (request,'account/delete_item.html',{'item':product})


def customer(request,pk):
 search=request.GET.get('search_bar') if request.GET.get('search_bar')!= None else ''	
 customer=Customer.objects.get(id=pk)	
 order2=customer.order_set.all()
 order=customer.order_set.filter(
	Q(product__name__icontains=search)|
  Q(status__icontains=search)
 )
 total_orders=order2.count()
 context={'customer':customer,'orders':order,'total_orders':total_orders,'orders2':order2}
 return render (request,'account/customer.html',context)


def update_customer(request,pk):
	customer=Customer.objects.get(id=pk)
	form=CustomerForm(instance=customer)
	if request.method == 'POST':
		form=CustomerForm(request.POST,instance=customer)
		if form.is_valid():
			form.save()
			return redirect ('customer',pk=customer.id)
	context={'forms':form,}
	return render (request,'account/customer_form.html',context)


def delete_customer(request,pk):
	customer=Customer.objects.get(id=pk)
	if request.method == 'POST':
		customer.delete()
		return redirect ('dashboard')
	return render (request,'account/delete_item.html',{'item':customer})


def create_order(request,pk):
	customer=Customer.objects.get(id=pk)
	form=OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('customer',pk=customer.id)
	context={'forms':form}
	return render (request,'account/order_form.html',context)


def update_order(request,pk):
	order=Order.objects.get(id=pk)
	form=OrderForm(instance=order)
	if request.method == 'POST':
		form=OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect ('dashboard')
	context={'order':order,'forms':form}
	return render (request,'account/order_form.html',context)	


def delete_order(request,pk):
	order=Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect ('dashboard')
	context={'item':order}	
	return render (request,'account/delete_item.html',context)	