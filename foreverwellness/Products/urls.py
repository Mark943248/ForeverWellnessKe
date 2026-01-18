from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('category/<str:category>/', views.product_by_category, name='product_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail')
]