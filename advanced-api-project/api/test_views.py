# api/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book, Author
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for testing and authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Use self.client.login to simulate user login
        self.client.login(username='testuser', password='testpass')  # This line ensures the client is logged in

        # Create an author for testing
        self.author = Author.objects.create(name="George Orwell")

        # Create some book entries for testing
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

        # Set up URLs for testing CRUD operations
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # Example test cases to ensure correct functionality
    def test_list_books(self):
        # Test to ensure the book list view returns the correct status code and data
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        # Test creating a new book entry
        data = {
            "title": "Brave New World",
            "publication_year": 1932,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Brave New World")

    def test_update_book(self):
        # Test updating an existing book
        data = {
            "title": "1984 Updated",
            "publication_year": 1949,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "1984 Updated")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)