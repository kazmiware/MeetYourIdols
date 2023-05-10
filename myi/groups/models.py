from django.db import models
from django.urls import reverse
from user.models import (Alumni, Student)
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    post_std = models.ForeignKey(Student, null=True, on_delete=models.CASCADE,
                             related_name="post_std")
    post_alm = models.ForeignKey(Alumni, null=True, on_delete=models.CASCADE,
                             related_name="post_alm")
    text = models.TextField(max_length=200)
    image = models.ImageField(upload_to='posts/images', null=True)
    video = models.FileField(upload_to='posts/videos', null=True)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)


class Group(models.Model):

    admin = models.ForeignKey(User, null=True, on_delete=models.CASCADE, 
                              related_name="group_admin")
    banner = models.ImageField(upload_to="group_images/banners", null=True)
    image = models.ImageField(upload_to="group_images/main_images", null=True)
    name = models.CharField(max_length=50, default="Your Group")
    field = models.CharField(max_length=50, default="Electrical")
    des = models.CharField(max_length=150, default="None")
    posts = models.ManyToManyField(Post)
    date = models.DateField(null=True)
    alumnis = models.ManyToManyField(Alumni)
    students = models.ManyToManyField(Student)


    def get_post_url(self):

        return reverse("add_post", kwargs={'pk':self.pk})
