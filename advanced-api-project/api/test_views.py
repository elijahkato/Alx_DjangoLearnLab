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
        # Create a user and obtain a token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create some books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

        # Set up URLs for CRUD operations
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        # Test listing all books
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        # Test creating a new book
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

    def test_search_books(self):
        # Test searching for books by title
        response = self.client.get(f'{self.book_list_url}?search=1984')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_order_books(self):
        # Test ordering books by publication year
        response = self.client.get(f'{self.book_list_url}?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')
        self.assertEqual(response.data[1]['title'], '1984')

    def test_permissions(self):
        # Test access control: Ensure unauthenticated requests cannot create a book
        self.client.force_authenticate(user=None)  # Log out the authenticated user
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
