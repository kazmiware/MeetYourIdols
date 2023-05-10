from rest_framework.generics import (CreateAPIView, RetrieveAPIView, 
                                     UpdateAPIView)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .serializers import (AlumniSerializer, StudentSerializer)
from .models import (Alumni, Student)


class AlumniCreateApiView(CreateAPIView):

    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer

    def perform_create(self, serializer):

        if serializer.is_valid():

            user = self.request.POST.get('user')
            user = get_object_or_404(User, username=user)
            field = serializer.validated_data['field']
            serializer.save(user=user)
        return super().perform_create(serializer)
    

class StudentCreateApiView(CreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):

        print(serializer.is_valid())
        if serializer.is_valid():

            user = self.request.POST.get('user')
            user = get_object_or_404(User, username=user)
            field = serializer.validated_data['field']
            serializer.save(user=user)
        return Response(serializer.data)


class AlumniRetrieveApiView(RetrieveAPIView):

    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer



class StudentRetrieveApiView(RetrieveAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer 


class StudentUpdateApiView(UpdateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def perform_update(self, serializer):

        if serializer.is_valid():

            field = serializer.validated_data['field']
            uni = serializer.validated_data['uni']
            about = serializer.validated_data['about']
            serializer.save(field=field, uni=uni, about=about)   
        return Response(serializer.data)\


class AlumniUpdateApiView(UpdateAPIView):

    queryset = Alumni.objects.all()
    serializer_class = StudentSerializer


    def perform_update(self, serializer):

        if serializer.is_valid():

            field = serializer.validated_data['field']
            exp = serializer.validated_data['experience']
            uni = serializer.validated_data['uni']
            about = serializer.validated_data['about']
            serializer.save(field=field, uni=uni, about=about, experience=exp)   
        return Response(serializer.data)                           

