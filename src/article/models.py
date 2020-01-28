from django.db import models
from django.contrib.auth.models import User#imported log_in, log_out, register, session module 

# Create your models here.

class Post(models.Model):
  header = models.CharField(max_length=50)#CharField = small str file
  content = models.TextField(max_length=3000)#TextField = large str file
  draft = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)#auto_now_add = time(Post has been added)
  updated = models.DateTimeField(auto_now=True)#auto_now = time(Post's last update)
  image = models.ImageField(blank=True)#not obligatory to add (blank = True)
  liked = models.PositiveSmallIntegerField(default=0)
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='articles')
  #on_delete=models.CASCADE deletes all posts of this owner when the owner's acc is deleted

  def __str__(self):
    return self.header#customizes visible name on adminpanel 

class Comment(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField(max_length=280)
  post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
  
  def __str__(self):
    return self.title#customizes visible name on adminpanel

class Created(models.Model):
  content = models.CharField(max_length=50)