from django.urls import path
from . views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('adminsite/', AdminProductListView.as_view(),name='adminsite'),
	path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('add/', ProductCreateView.as_view(), name='product-create'),

    path('admin_login/', auth_views.LoginView.as_view(template_name='auth/admin_login.html'),name='admin_login'),
	path('admin_logout/', auth_views.LogoutView.as_view(template_name='auth/admin_logout.html'),name='admin_logout'),
]
