# api/urls.py
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books', BookViewSet, basename='book')

# Define the URL patterns for both BookList view and the router's URLs
urlpatterns = [
    path('booklist/', BookList.as_view(), name='book-list'),  # Keep this if you need BookList
    # Include the URLs managed by the router (this handles all CRUD operations for BookViewSet)
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
