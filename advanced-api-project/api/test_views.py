# api/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Log in the test client with the user credentials
        self.client.login(username='testuser', password='testpass')  # Correct use of self.client.login

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create some books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

        # Set up URLs for CRUD operations
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # Your test cases go here...
