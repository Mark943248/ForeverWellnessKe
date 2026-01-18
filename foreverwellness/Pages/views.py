from django.shortcuts import render
from Products.models import Product
from Blog.models import Blog

# Create your views here.
def home(request):
    products = Product.objects.all().order_by('-posted_at')[:6]  # Display latest 6 products
    blogs = Blog.objects.filter(published=True).order_by('-posted_at')[:6]  # Display latest 6 blogs
    return render(request, 'pages/index.html', {'products': products, 'blogs': blogs})

# View for About Us page
def about(request):
    return render(request, 'pages/about.html')

# View for Contact Us page
def contact(request):
    return render(request, 'pages/contact.html')