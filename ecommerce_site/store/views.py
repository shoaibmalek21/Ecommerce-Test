from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from . models import *
from . utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json
import datetime


class home(View):
	def get(self,request):
		
		data = cartData(request)
		cartItems = data['cartItems']
			
		products = Product.objects.all() 
		context = {'products':products,'cartItems':cartItems}
		return render(request, 'index.html',context)


class ProductListView(ListView):
	model = Product
	template_name = 'index.html'
	context_object_name = 'queryset'
	ordering = ['-name']


class ProductListView(ListView):
	model = Product
	template_name = 'index.html'
	context_object_name = 'queryset'
	ordering = ['-name']

def store(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	# data = cartData(request)
	# cartItems = data['cartItems']
	# order = data['order']
	# items = data['items']
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = data['get_cart_items']



	# data = cartData(request)
	# cartItems = data['cartItems']
		
	# products = Product.objects.all() 
	context = {'products':products,'cartItems':cartItems}
	return render(request, 'store/index.html', context)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items


	# data = cartData(request)
	# cartItems = data['cartItems']
	# order = data['order']
	# items = data['items']
	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = data['get_cart_items']


	# context = {'items':items, 'order':order}
	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request, 'cart.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	# data = cartData(request)
	# cartItems = data['cartItems']
	# order = data['order']
	# items = data['items']

	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = data['get_cart_items']


	# context = {'items':items, 'order':order}
	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request, 'checkout.html', context)



def updateItem(request):
	data = json.loads(request.body)
	product_id = data['productId']
	action = data['action']

	print('Action:', action)
	print('productId:', product_id)

	customer = request.user.customer
	product = Product.objects.get(id=product_id)
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
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		
	else:
		customer, order = guestOrder(request, data)
		
	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == float(order.get_cart_total):
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
				customer=customer,
				order=order,
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				zipcode=data['shipping']['zipcode'],
		)


	return JsonResponse('Payment complete!', safe=False)
