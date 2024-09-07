from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)  # Use a tuple with a trailing comma or a list

# Explicitly register the Book model with the admin interface
admin.site.register(Book, BookAdmin)
