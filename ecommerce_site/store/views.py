from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from . models import Product
from . utils import cartData



class home(View):
	def get(self,request):
		# context = {
		# 	queryset : Product.objects.all()
		# }
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

class ProductDetailView(DetailView):
	model = Product

class ProductCreateView(CreateView):
	model = Product
	fields = ['name','image','price']


class ProductUpdateView(UpdateView):
	model = Product
	fields = ['name','image','price']


class ProductDeleteView(DeleteView):
	model = Product
	success_url = '/'


def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order,'cartItems':cartItems}
	return render(request, 'cart.html', context)


class AdminSite(View):
	def get(self,request):
		context = {
			products : Product.objects.all()
		}
		return render(request, 'adminsite.html',context)


class AdminProductListView(ListView):
	model = Product
	template_name = 'adminsite.html'
	context_object_name = 'products'
	ordering = ['-name']
