from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout/', views.logout_user, name='logout'),
]