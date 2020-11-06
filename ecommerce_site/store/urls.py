from django.urls import path
from . views import *
from . import views

urlpatterns = [
	# path('', views.home.as_view(),name='home'),
	path('', ProductListView.as_view(),name='store-home'),
	path('adminsite/', AdminProductListView.as_view(),name='adminsite'),
	path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('add/', ProductCreateView.as_view(), name='product-create'),

	path('cart/', views.cart, name='cart'),
	path('checkout/', views.checkout, name='checkout'),
	path('update_item/', views.updateItem, name='update_item'),
	path('process_oder/', views.processOrder, name='process_order')
]
