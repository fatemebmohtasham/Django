from django.forms import ModelForm
from .models import Customer, Order,Product,User
from django.contrib.auth.forms  import UserCreationForm


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','name','phone','email','password1','password2']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'		