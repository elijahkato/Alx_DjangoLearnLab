from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()  # Add tagging functionality

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link each comment to a post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each comment to the user who made it
    content = models.TextField()  # The content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the comment is first created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when the comment is modified

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
