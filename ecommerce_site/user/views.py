from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegitrationForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View

@csrf_protect
def RegistrationView(request):
	if request.method == 'POST':
		form = UserRegitrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request,f'Account Create {username}.')
			return redirect('login')

	else:
		form = UserRegitrationForm()

	return render(request,'auth/register.html',{'form':form})


@csrf_protect
class LoginView(View):
	def get(self, request):
		return render(request,'auth/login.html')