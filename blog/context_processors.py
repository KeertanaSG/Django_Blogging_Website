from .models import Post

def trending_posts(request):
    trending_posts = Post.objects.order_by('-views')[:5]
    context = {
        'trending_posts': trending_posts,
    }
    return context