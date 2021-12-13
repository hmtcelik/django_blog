from django.urls import path, include
from .views import BlogView, PostView, PostCreateView


urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('<int:pk>/', PostView.as_view(), name="post" ),
    path('new/', PostCreateView.as_view(), name="postnew" ),    
]
