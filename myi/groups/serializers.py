from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import (Post, Group)


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    def get_name(self):

        return self.context.get('request').user.username


class AlumniSerializer(serializers.Serializer):

    profile_image = serializers.ImageField(use_url=False)
    user = UserSerializer(read_only=True)


class StudentSerializer(serializers.Serializer):

    profile_image = serializers.ImageField(use_url=False)
    user = UserSerializer(read_only=True)


class PostGroupSerializer(serializers.Serializer): 

    post_std = StudentSerializer(read_only=True)
    post_alm = AlumniSerializer(read_only=True)
    text = serializers.CharField()
    image = serializers.ImageField(use_url=True)
    video = serializers.FileField(use_url=True)
    likes = serializers.IntegerField()
    shares = serializers.IntegerField()
    

class GroupSerializer(serializers.ModelSerializer):

    admin = UserSerializer(read_only=True)
    name = serializers.CharField()
    field = serializers.CharField()
    des = serializers.CharField()
    posts = PostGroupSerializer(read_only=True, many=True)
    date = serializers.DateField(read_only=True)
    alumnis = AlumniSerializer(read_only=True, many=True)
    students = StudentSerializer(read_only=True, many=True) 
    add_post = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Group
        fields = [
            'admin',
            'name',
            'field',
            'des',
            'posts',
            'date',
            'alumnis',
            'students',
            'add_post'
        ]

    def get_add_post(self, obj):


        return reverse("add_post", kwargs={'pk':obj.pk})   
          

