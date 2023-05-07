from typing import Any, Optional
from django.db import models
from django.shortcuts import (render, get_object_or_404, redirect)
from django.views.generic import (View, DetailView, CreateView)
from django.contrib.auth.models import User
import requests
import datetime

from .models import (Post, Group)
from user.models import (Alumni, Student)
from .forms import (PostForm, GroupForm)

# Create your views here.

class AddPostView(View):

    def get(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)
        return render(request, 'groups/post_add.html', {'form':form})
    

    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)
        self.form_valid(form)
        form = PostForm()
        return render(request, 'groups/post_add.html', {'form':form})
    

    def form_valid(self, form):      
           
        if form.is_valid():
            text = form.cleaned_data['text']
            img = self.request.FILES.get('image')
            vid = self.request.FILES.get('video')
            user = get_object_or_404(Student, user=self.request.user)
            if user:
                post = Post(text=text, post_std=user)
            else:
                user = get_object_or_404(Alumni, user=self.request.user)
                post = Post(text=text, post_alm=user)  
            if img != None:
                post.image.save(img.name, img, save=True)
            if vid !=None:  
                post.video.save(vid.name, vid, save=True)
            post.save()
            group = self.get_object()
            group.posts.add(post)
            return redirect(f"/group/detail/{self.kwargs.get('pk')}")
        return False   


    def get_object(self):

        pk = self.kwargs.get('pk')
        group = get_object_or_404(Group, pk=pk)
        return group


class GroupDetailView(DetailView) :

    queryset = Group.objects.all()
    template_name = "groups/group_dt.html"


    def get_object(self):
        
        pk =self.kwargs.get('pk')
        response  = requests.get(f'http://127.0.0.1:8000/api/group/detail/{pk}')
        alumnis = response.json()['alumnis']
        obj = response.json()
        obj['alumni_image'] = []
        for alumni in alumnis:
           user  = get_object_or_404(User, username=alumni['user']['username'])
           user = get_object_or_404(Alumni, user=user)
           obj['alumni_image'].append(user.profile_image.url)
        print(obj)
        return obj
    

class GroupCreateView(CreateView):

    queryset = Group.objects.all()
    form_class = GroupForm
    template_name = 'groups/group_cr.html'
    success_url = "/group" 

    def form_valid(self, form):

        if form.is_valid():

           name = form.cleaned_data['name']
           field = form.cleaned_data['field'] 
           des = form.cleaned_data['des']
           date = datetime.date.today()
           data = {
               'pk': self.request.user.pk,
               'name': name,
               'field': field,
               'des': des,
               'date': date
           }
           response  = requests.post('http://127.0.0.1:8000/api/group',
                                    data=data) 
        return redirect(self.success_url)  





