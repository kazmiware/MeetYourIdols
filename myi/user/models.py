from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CHOICES = [("Student", "Student"), ("Alumni", "Alumni")]


class Alumni(models.Model):

    banner_image = models.ImageField(upload_to='profile_pics/alumnis', default="profile_pics/default.jpg")
    profile_image = models.ImageField(upload_to='profile_pics/alumnis', default="profile_pics/default.jpg")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, 
                             related_name="alumni_user")
    field = models.CharField(max_length=50)
    experience = models.IntegerField()
    uni = models.CharField(max_length=50, default="Ned", null=True)
    about = models.TextField(max_length=150)


class Student(models.Model):

    banner_image = models.ImageField(upload_to='profile_pics/students', default="profile_pics/default.jpg")
    profile_image = models.ImageField(upload_to='profile_pics/students', default="profile_pics/default.jpg")
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, 
                             related_name="student_user")
    field = models.CharField(max_length=50)
    uni = models.CharField(max_length=50, default="Ned", null=True)
    about = models.TextField(max_length=150)    