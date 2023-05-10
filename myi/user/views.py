from typing import Any, Optional
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic import (View, CreateView, UpdateView)
from django.contrib.auth.models import User
from django.contrib.auth import (login, authenticate)
import requests

from .forms import (SignUpForm, AlumniForm, StudentForm, LoginForm)
from .models import (Alumni, Student)
from groups.models import (Post, Group)
# Create your views here.

class UserCreateView(View):


    def get(self, request, *args, **kwargs):

        form = SignUpForm(request.POST or None)
        return render(request, "registration/signup.html", {'form':form})
    

    def post(self, request, *args, **kwargs):

        form = SignUpForm(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            choice = form.cleaned_data['choice']
            password = form.clean_password2()
            user = User(username=name, email=email,)
            user.save()
            user.set_password(password)
            user.save()
            user = authenticate(username=name, password=password)
            if user:
                login(request, user)
                if choice == 'Student':
                    return redirect('/student')
                return redirect('/alumni')
        return render(request, "registration/signup.html", {'form':form})
    

class UserLoginView(View):

    def get(self, request, *args, **kwargs):

        form = LoginForm(request.POST or None)
        return render(request, 'registration/login.html', {'form':form})
    

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST or None)
        print(form.is_valid())
        if form.is_valid():

            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=name, password=password)
            print(user)
            if user:
                print(user)
                login(request, user)
                return redirect('/')
        return render(request, 'registration/login.html', {'form':form})  

    

class AlumniCreateView(CreateView):

    template_name = "pages/user_cr.html"
    form_class =  AlumniForm
    queryset = Alumni.objects.all()
    success_url = "/user/alumni/detail"

    def form_valid(self, form):

        if form.is_valid():
            field = form.cleaned_data['field']
            experience = form.cleaned_data['experience']
            about = form.cleaned_data['about']
            uni = form.cleaned_data['uni']
            data = {
                'user':self.request.user,
                'field':field,
                'experience':experience,
                'uni':uni,
                'about':about
            }
            response = requests.post('http://127.0.0.1:8000/user/api/alumni', data=data)
        return redirect(self.success_url + f"/{self.save_files(self.request)}")
    

    def save_files(self, request):

        obj = Alumni.objects.last()
        print(request.FILES)
        banner = request.FILES.get('banner_image')
        img = request.FILES.get('profile_image')
        if banner != None:
           obj.banner_image.save(banner.name, banner, save=True) 
        if img != None:   
           obj.profile_image.save(img.name, img, save=True) 
        obj.save()
        return obj.pk 



class StudentCreateView(CreateView):

    template_name = "pages/user_cr.html"
    form_class =  StudentForm
    queryset = Student.objects.all()
    success_url = "/user/student/detail"

    def form_valid(self, form):

        if form.is_valid():
            field = form.cleaned_data['field']
            about = form.cleaned_data['about']
            uni = form.cleaned_data['uni']
            data = {
                'user':self.request.user,
                'field':field,
                'uni':uni,
                'about':about,
            }
            response = requests.post('http://127.0.0.1:8000/user/api/student', data=data)  
            print(response.status_code) 
        return redirect(self.success_url + f"/{self.save_files(self.request)}") 
    

    def save_files(self, request):

        obj = Student.objects.last()
        print(request.FILES)
        banner = request.FILES.get('banner_image')
        img = request.FILES.get('profile_image')
        if banner != None:
           obj.banner_image.save(banner.name, banner, save=True) 
        if img != None:   
           obj.profile_image.save(img.name, img, save=True) 
        obj.save()
        return obj.pk


class AlumniDetailView(View):

    queryset = Alumni.objects.all()
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        obj = self.get_object(pk)
        init = {
            'field': obj['field'],
            'experience': obj['experience'],
            'uni': obj['uni'],
            'about': obj['about']
        }
        form = AlumniForm(request.POST or None, initial=init)
        return render(request, "pages/user_dt.html", {"object":obj, "form":form})
    
    
    def post(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        form = AlumniForm(request.POST or None)
        self.form_valid(form, pk)
        obj = self.get_object(pk)
        return render(request, "pages/user_dt.html", {"object":obj, "form":form})
    

    def get_object(self, pk):
        
        response = requests.get(f'http://127.0.0.1:8000/user/api/alumni/detail/{pk}')
        obj = response.json()
        object = get_object_or_404(Alumni, pk=pk)
        profile_image = object.profile_image.url
        banner_image = object.banner_image.url
        obj['profile_image'] = profile_image
        obj['banner_image'] = banner_image
        return obj
    

    def form_valid(self, form, pk):

        if form.is_valid():
            
            field = form.cleaned_data['field']
            uni = form.cleaned_data['uni']
            about = form.cleaned_data['about']
            data = {
                'field': field,
                'uni': uni,
                'about': about
            }
            response = requests.put(f'http://127.0.0.1:8000/user/api/student/update/{pk}',
                                    data=data)      

class StudentDetailView(View):

    queryset = Student.objects.all()
    template_name = "pages/user_dt.html"

    
    def get(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        obj = self.get_object(pk)
        init = {
            'field': obj['field'],
            'uni': obj['uni'],
            'about': obj['about']
        }
        form = StudentForm(request.POST or None, initial=init)
        return render(request, "pages/user_dt.html", {"object":obj, "form":form})
    

    def post(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        form = StudentForm(request.POST or None)
        self.form_valid(form, pk)
        obj = self.get_object(pk)
        return render(request, "pages/user_dt.html", {"object":obj, "form":form})


    def get_object(self, pk):
        
        response = requests.get(f'http://127.0.0.1:8000/user/api/student/detail/{pk}')
        obj = response.json()
        object = get_object_or_404(Student, pk=pk)
        profile_image = object.profile_image.url
        banner_image = object.banner_image.url
        obj['profile_image'] = profile_image
        obj['banner_image'] = banner_image
        return obj
    

    def form_valid(self, form, pk):
 
        if form.is_valid():
           
           field = form.cleaned_data['field']
           uni = form.cleaned_data['uni']
           about = form.cleaned_data['about']
           data = {
               'field': field,
               'uni': uni,
               'about': about
           }
           response = requests.put(f'http://127.0.0.1:8000/user/api/student/update/{pk}',
                                   data=data)
                

          
class AlumniUpdateView(UpdateView):        

    queryset = Alumni.objects.all() 
    template_name = "pages/user_cr.html"
    form_class = AlumniForm
    success_url = "user/alumni/detail"
    

    def form_valid(self, form):

        pk = self.kwargs.get('pk')
        if form.is_valid():
            field = form.cleaned_data['field']
            experience = form.cleaned_data['experience']
            about = form.cleaned_data['about']
            uni = form.cleaned_data['uni']
            data = {
                'user':self.request.user,
                'field':field,
                'experience':experience,
                'uni':uni,
                'about':about
            }
            response = requests.post(f'http://127.0.0.1:8000/user/api/alumni/update/{pk}', 
                                     data=data)
        return redirect(self.success_url + f"/{self.save_files(self.request)}")
    

    def get_object(self, queryset):
        return super().get_object(queryset)
    

    def save_files(self, request):

        obj = Alumni.objects.last()
        print(request.FILES)
        banner = request.FILES.get('banner_image')
        img = request.FILES.get('profile_image')
        if banner != None:
            obj.banner_image.save(banner.name, banner, save=True) 
        if img != None:   
            obj.profile_image.save(img.name, img, save=True) 
        obj.save()
        return obj.pk
    

class StudentUpdateView(UpdateView):        

    queryset = Student.objects.all() 
    template_name = "pages/user_cr.html"
    form_class = StudentForm
    success_url = "user/student/detail"

    def form_valid(self, form):

        pk = self.kwargs.get('pk')
        if form.is_valid():
            field = form.cleaned_data['field']
            experience = form.cleaned_data['experience']
            about = form.cleaned_data['about']
            uni = form.cleaned_data['uni']
            data = {
                'user':self.request.user,
                'field':field,
                'experience':experience,
                'uni':uni,
                'about':about
            }
            response = requests.post(f'http://127.0.0.1:8000/user/api/student/update/{pk}', 
                                     data=data)
        return redirect(self.success_url + f"/{self.save_files(self.request)}")
    
    
    def get_object(self):

        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Student, pk=pk) 
        return obj
    

    def save_files(self, request):

        obj = Student.objects.last()
        print(request.FILES)
        banner = request.FILES.get('banner_image')
        img = request.FILES.get('profile_image')
        if banner != None:
            obj.banner_image.save(banner.name, banner, save=True) 
        if img != None:   
            obj.profile_image.save(img.name, img, save=True) 
        obj.save()
        return obj.pk    

     