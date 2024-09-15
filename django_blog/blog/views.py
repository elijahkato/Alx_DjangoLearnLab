# blog/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

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
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for displaying the list of posts
    context_object_name = 'posts'
    ordering = ['-published_date']  # Orders posts by date (most recent first)

# DetailView to display individual post details
class PostDetailView(DetailView):
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
