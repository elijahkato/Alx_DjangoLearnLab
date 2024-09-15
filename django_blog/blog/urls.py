from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import profile_view,  CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search_view, PostByTagListView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registration URL
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),  # Login URL
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Logout URL
    path('profile/', profile_view, name='profile'),  # Profile view URL
    path('', PostListView.as_view(), name='post-list'),  # URL for listing posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # URL for post details
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # URL for creating a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-edit'),  # URL for editing a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # URL for deleting a post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create a new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Update an existing comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
     path('search/', search_view, name='search'),  # Search view URL
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),  # URL for filtering posts by tag
]
