from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    
#  GELDIGINDE NOT !!!!!!!!!!!  BURAYA BLOG DIYE MODELDE AC ONLARI ONLARA KOYARAK DENE BISILER YAP