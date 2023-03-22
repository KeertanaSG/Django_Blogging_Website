from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm, UpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Category



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.views += 1
        post.save()
        return super().get(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.header_image = self.request.FILES.get('header_image')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = UpdateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class TopPostsListView(ListView):
    model = Post
    template_name = 'blog/top_posts.html' 
    context_object_name = 'trending_posts'
    ordering = ['-views']
    paginate_by = 5

    def get_queryset(self):
        # Get the posts with the most page views in the last 30 days
        start_date = timezone.now() - timezone.timedelta(days=30)
        return Post.objects.filter(date_posted__gte=start_date).order_by('-views')[:5]
    
    
class CategoryListView(ListView):
    model = Category
    template_name = 'blog/discover.html'
    context_object_name = 'categories'


def info(request):
    return render(request, 'blog/blog-info.html', {'title': 'About Us'})

def discover(request):
    return render(request, 'blog/discover.html', {'title': 'Discover'})

def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request,'blog/categories.html', {'cats': cats, 'category_post': category_post})