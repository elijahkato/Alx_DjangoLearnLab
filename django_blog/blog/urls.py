# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # URL for listing posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # URL for post details
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # URL for creating a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),  # URL for editing a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # URL for deleting a post
]
