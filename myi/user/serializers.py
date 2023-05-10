from rest_framework import serializers

from .models import (Alumni, Student)

class UserSerializer(serializers.Serializer):

    name = serializers.SerializerMethodField()

    def get_name(self, user):

        return user.username
    

class AlumniSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    field = serializers.CharField()
    experience = serializers.IntegerField()
    uni = serializers.CharField()
    about = serializers.CharField()

    class Meta:

        model = Alumni
        fields = [
            'user',
            'field',
            'experience',
            'uni',
            'about'
        ]


class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    field = serializers.CharField()
    uni = serializers.CharField()
    about = serializers.CharField()

    class Meta:

        model = Student
        fields = [
            'user',
            'field',
            'uni',
            'about'
        ]        