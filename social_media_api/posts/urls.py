from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
path('feed/', UserFeedView.as_view(), name='user-feed'),

urlpatterns = [
    path('', include(router.urls)),
]
