from django import forms

from .models import (Post, Group)


class PostForm(forms.ModelForm):

    text = forms.CharField(max_length=200, required=False,
                           widget=forms.Textarea(
                                                     attrs = {
                                                               'placeholder':
                                                               "Write something"
                                                             } 
                                                  ))
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)

    class Meta:

        model = Post
        fields = [
            'text',
            'image',
            'video'
        ] 


class GroupForm(forms.ModelForm):

    name = forms.CharField(max_length=50,
                            widget=forms.TextInput(
                                                     attrs = {
                                                               'placeholder':
                                                               "Your group name"
                                                             } 
                                                  )
                            )
    field = forms.CharField(max_length=50, 
                            widget=forms.TextInput(
                                                     attrs = {
                                                               'placeholder':
                                                               "Your group field"
                                                             } 
                                                  )
                           )
    des = forms.CharField(max_length=150, 
                          widget=forms.Textarea(
                                                  attrs = {
                                                            'placeholder':
                                                            "Your Description"
                                                          }
                                               )
    )

    class Meta:

        model = Group
        fields = [
            'name',
            'field'
        ]         