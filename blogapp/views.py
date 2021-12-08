from django.views.generic import TemplateView
from .models import Post


class BlogView(TemplateView):
    template_name = 'blog.html'
    context_object_name = 'all_posts'
    model = Post
    
    def get_queryset(self):
        return Post.objects.all()
    
class PostView(TemplateView):
    template_name = 'post.html'
    model = Post
    
