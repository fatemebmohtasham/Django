from django.forms import ModelForm
from .models import Customer, Order,Product
from django.contrib.auth.models  import User
from django.contrib.auth.forms  import UserCreationForm


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class OrderUser(ModelForm):
	class Meta:
		model = Order
		fields = ['product','status']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'		