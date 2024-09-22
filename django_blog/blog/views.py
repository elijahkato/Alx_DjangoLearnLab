# blog/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.utils.decorators import method_decorator
from django.db.models import Q
from taggit.models import Tag

def profile_view(request):
    if request.method == 'POST':  # Check if the request is a POST request
        form = ProfileUpdateForm(request.POST, instance=request.user)  # Pass the logged-in user to update their details
        if form.is_valid():  # Validate the form data
            form.save()  # Save the updated user information
            return redirect('profile')  # Redirect back to the profile page after saving
    else:
        form = ProfileUpdateForm(instance=request.user)  # Display the form with the current user data

    return render(request, 'blog/profile.html', {'form': form})


# Custom Registration View
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = '/login/'  # Redirect to login after registration

# Profile Management View
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'blog/profile.html'
    success_url = '/profile/'  # Redirect to the profile page after update

    def get_object(self):
        # Only allow the logged-in user to update their profile
        return self.request.user

# ListView to display all blog posts
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for displaying the list of posts
    context_object_name = 'posts'
    ordering = ['-published_date']  # Orders posts by date (most recent first)

# DetailView to display individual post details
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for displaying a single post

# CreateView to create a new post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use custom form for creating posts
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current logged-in user
        return super().form_valid(form)

# UpdateView to edit an existing post (author only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit their post

# DeleteView to delete a post (author only)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect to the post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete their post

# Comment Create View
@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})

# Comment Update View
@method_decorator(login_required, name='dispatch')
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

# Comment Delete View
@method_decorator(login_required, name='dispatch')
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


def search_view(request):
    query = request.GET.get('q')
    results = Post.objects.none()  # Start with an empty queryset

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Reuse the post list template
    context_object_name = 'posts'

    def get_queryset(self):
        # Retrieve the tag from the URL slug and filter posts by this tag
        tag_slug = self.kwargs.get('tag_slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[tag])
    
    def get_context_data(self, **kwargs):
        # Pass the tag to the context for display in the template
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag_slug')
        return context