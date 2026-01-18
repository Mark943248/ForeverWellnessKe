from django.urls import path
from . import views

urlpatterns = [
    path('Blog_list/', views.Blog_list, name='blog_list'),
    path('Blog_detail/<slug:slug>/', views.Blog_detail, name='blog_detail'),
    path('blog_category/<str:category>/', views.Blog_by_category, name='blog_by_category'),
]