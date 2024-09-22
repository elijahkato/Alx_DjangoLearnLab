from django.contrib import admin
from .models import Post, Comment  # Import the Post and Comment models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Customize the columns displayed
    search_fields = ('title', 'content')  # Add search functionality
    list_filter = ('published_date', 'author')  # Add filtering options

# Register the Post model
admin.site.register(Post)

# (Optional) Register the Comment model if you want to manage comments as well
admin.site.register(Comment)