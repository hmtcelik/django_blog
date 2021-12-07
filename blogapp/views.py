from django.views.generic import TemplateView
from .models import Post


class BlogView(TemplateView):
    template_name = 'blog.html'
    
class PostView(TemplateView):
    template_name = 'post.html'
    
