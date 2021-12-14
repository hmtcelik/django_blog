from django.views.generic import TemplateView, ListView , DetailView, CreateView
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
    
class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = '__all__'
    
