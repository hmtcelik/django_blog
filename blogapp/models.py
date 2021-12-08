from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.CharField(max_length=20, default='01.01.2021')

    def __str__(self):
        return self.title
    
    