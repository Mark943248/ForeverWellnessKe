from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product
# Create your views here.

# View to display all products
def product_list(request):
    products = Product.objects.all().order_by('-posted_at')
    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(benefits__icontains=query) |
            Q(category__icontains=query)
        ).order_by('-posted_at')
    return render(request, 'products/product_list.html', {'products': products
                                                          , 'page_obj': page_obj})

# View to display product details
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # To dispaly related products based on category
    related_products = Product.objects.filter(
        category = product.category # Filter by same category
    ).exclude(id=product.id).order_by('-posted_at')[:6] # Limits n.o of products displayed in order of most recent

    return render(request, 'products/product_details.html', {'product': product, 'related_products': related_products})

# View to display products by category
def product_by_category(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'products/product_list.html', {'products': products, 'active_category': category})