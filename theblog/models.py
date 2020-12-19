from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255, default='coding')
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic= models.ImageField(null= True, blank= True, upload_to='images/')
    twitter= models.CharField(max_length=255, null=True, blank=True)
    instagram= models.CharField(max_length=255, null=True, blank=True)
    facebook= models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image= models.ImageField(null= True, blank= True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet=  models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='like_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title+' ' +'by' + ' '+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

class Comment(models.Model):
    post= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])