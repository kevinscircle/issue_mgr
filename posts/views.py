from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView,   
    UpdateView, 
    DeleteView,
)
from.models import Post, Status
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = (
            Post.objects
            .filter(status=Status.objects.get(name="published"))
            .order_by('created_on').reverse()
        )
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):    # key word arguements expanded 
        context = super().get_context_data(**kwargs)
        context['post_list'] = (
            Post.objects
            .filter(status=Status.objects.get(name="draft"))
            .order_by('created_on').reverse()
        )
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = (
            Post.objects
            .filter(status=Status.objects.get(name="archived"))
            .order_by('created_on').reverse()
            )
        return context
    
class DetailPostView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def test_func(self):
        post = self.get_object()
        if post.status.name == "published" or post.status.name == "archived":
            return True
        elif post.status.name == "draft" and post.author == self.request.user:
            return True
        else:
            return False
        

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'status', 'body']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

            
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'status', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

