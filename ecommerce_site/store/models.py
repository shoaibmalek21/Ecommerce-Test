from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return '%s' % (self.name)

class SubCategory(models.Model):
	name = models.CharField(max_length=200, null=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,primary_key=True)


	def __str__(self):
		return '%s' % (self.name)

class Product(models.Model):
	# SEL_ID = models.AutoField(db_column='SEL_ID',primary_key=True)
	PRO_ID = models.IntegerField(null=True)
	name = models.CharField(max_length=200, null=True)
	# sub_category = models.OneToOneField(Category,on_delete=models.CASCADE,primary_key=True)
	category = models.ForeignKey(SubCategory, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
	# subcategory = models.ForeignKey(SubCategory, related_name='category', on_delete=models.CASCADE, blank=True, null=True)
	# subcategory = GenericForeignKey(SubCategory, category)
	# subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

	# sub_category = models.OneToOneField(SubCategory,on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)
	price = models.FloatField()
	# category = models.OneToOneField(Category,on_delete = models.CASCADE) 

	# category = models.OneToOneField(Category,on_delete=models.CASCADE)
	# subcategory = models.OneToOneField(SubCategory,on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.name)


	def get_absolute_url(self):
	    return reverse('product-detail', kwargs={'pk':self.pk})

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = "images/placeholder.jpg"
		return url 



class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return f'{self.user}'


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)	
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return "Order {} - {}".format(self.id, self.customer)	

	# @property
	# def shipping(self):
	# 	shipping = False
	# 	orderitems = self.orderitem_set.all()
	# 	for i in orderitems:
	# 		if i.product == False:
	# 			shipping = True
	# 	return shipping
	
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.product, self.order)	

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.city, self.order)	

