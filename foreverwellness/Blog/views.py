from django.shortcuts import render
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def Blog_list(request):
    blogs = Blog.objects.filter(published=True).order_by('-posted_at')
    recently_added = Blog.objects.filter(published=True).order_by('-posted_at')[:5]
    featured_blog = Blog.objects.filter(published=True, featured=True).order_by('-posted_at').first()
    paginator = Paginator(blogs, 10)  # Show 10 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query = request.GET.get('q')
    if query:
        blogs = Blog.objects.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(content__icontains=query) |
            Q(category__icontains=query)
        ).order_by('-posted_at')

    return render(request, 'Blog/Blog_list.html', { 
                                                   'blogs': blogs, 
                                                   'recently_added': recently_added, 
                                                   'featured_blog': featured_blog,
                                                    'page_obj': page_obj
                                                   })

def Blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug, published=True)
    related_blogs = Blog.objects.filter(
        category=blog.category
    ).exclude(id=blog.id)[:6]  # Display 4 related articles
    return render(request, 'Blog/Blog_details.html', {'blog': blog, 'related_blogs': related_blogs})

def Blog_by_category(request, category):
    blogs = Blog.objects.filter(category=category, published=True).order_by('-posted_at')
    featured_blog = Blog.objects.filter(published=True, featured=True).first()
    return render(request, 'Blog/Blog_list.html', {'blogs': blogs, 'featured_blog': featured_blog})