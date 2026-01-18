from django.contrib import admin
from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'category', 'content', 'posted_at', 'published') # Display these fields in the admin list view
    prepopulated_fields = {'slug': ('title',)}  # Auto-fill slug from title
    search_fields = ('title', 'category', 'content') # Enable search by title, category, and content
    list_filter = ('published', 'posted_at') # Filter by published status and creation date
