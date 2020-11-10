from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'),name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'),name='logout'),
	path('Customer/', views.Customer,name='customer'),
	path('registration/', views.RegistrationView,name='registration'),
]
