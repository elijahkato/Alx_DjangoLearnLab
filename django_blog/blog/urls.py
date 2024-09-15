from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, ProfileUpdateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registration URL
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Logout URL
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('', PostListView.as_view(), name='post-list'),  # URL for listing posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # URL for post details
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # URL for creating a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),  # URL for editing a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # URL for deleting a post
]
