from django.views.generic import TemplateView, ListView , DetailView
from .models import Post


class BlogView(ListView):
    template_name = 'blog.html'
    context_object_name = 'all_posts'
    model = Post
    
    def get_queryset(self):
        return Post.objects.all()
    
class PostView(DetailView):
    template_name = 'post.html'
    model = Post
    
