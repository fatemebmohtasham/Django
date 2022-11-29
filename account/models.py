from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name
  
	def order(self):
		order_count = self.order_set.all().count()
		return order_count


class Product(models.Model):

	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True) 
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True )
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.product)