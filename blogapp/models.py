from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.CharField(max_length=20, default='01.01.2021')
    post_image = models.ImageField(upload_to="static/uploads", default="-")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse("post", args=[str(self.id)])
    