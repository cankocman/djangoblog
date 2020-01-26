from django.contrib import admin
from article.models import Post,Comment#imports manually added class objects

# Register your models here.
admin.site.register(Post)#Allows admin to add/edit posts
admin.site.register(Comment)#Allows admin to add/edit comments