from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from store.models import *
import datetime
from django.views.decorators.csrf import csrf_protect


class ProductDetailView(DetailView):
	model = Product

class ProductCreateView(CreateView):
	model = Product
	fields = ['PRO_ID','name','image','price','category']

class ProductUpdateView(UpdateView):
	model = Product
	fields = ['PRO_ID','name','image','price','category']

class ProductDeleteView(DeleteView):
	model = Product
	success_url = '/adminsite'


class AdminSite(View):
	def get(self,request):
		context = {
			products : Product.objects.all()
		}
		return render(request, 'adminsite.html',context)


class AdminProductListView(ListView):
	model = Product
	template_name = 'store/product_list_ad.html'
	context_object_name = 'products'
	# ordering = ['-id']


@csrf_protect
class LoginView(View):
	def get(self, request):

		return render(request,'auth/admin_login.html')

