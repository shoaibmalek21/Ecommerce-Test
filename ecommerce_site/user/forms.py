from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegitrationForm(UserCreationForm):
	SELLER_ID = forms.IntegerField()
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	address = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(label='Email', max_length=50)
	contact = forms.IntegerField(required=False)
	city = forms.CharField(max_length=20, required=False)

	class Meta:
		model = User
		fields = ['SELLER_ID','first_name','last_name','username','email','address','password1','password2','contact','city']
