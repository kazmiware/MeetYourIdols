from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django import forms
from django.contrib.auth.models import User

from .models import (Alumni, Student)

CHOICES = [("Student", "Student"), ("Alumni", "Alumni")]


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
              'placeholder': "Enter Your Username"
            }
        )
        self.fields['email'].widget.attrs.update(
            {
              'placeholder': "Enter Your Email"
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
              'placeholder': "Enter Your Password"
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
              'placeholder': "Confirm Password"
            }
        )

    choice = forms.ChoiceField(choices=CHOICES)

    class Meta:
      
        model = User
        fields = ['username',
                  'email']      
        

class AlumniForm(forms.ModelForm):

    profile_image = forms.ImageField()
    banner_image = forms.ImageField()
    field = forms.CharField(max_length=50, label="Field",
                            widget=forms.TextInput(
                                                   attrs={
                                                         "placeholder":"Your Field"
                                                        }
                                                )
                            )
    experience = forms.IntegerField(label="Experience",   
                                    widget=forms.TextInput(
                                                  attrs={
                                                         "placeholder":"Your Work Experience"
                                                        }
                                                )
                                    )
    uni = forms.CharField(max_length=50, label="University",
                          widget=forms.TextInput(
                                                  attrs={
                                                         "placeholder":"Your University"
                                                        }
                                                )
                          )
    about = forms.CharField(max_length=150, 
                            widget=forms.Textarea(
                                                attrs={
                                                        "placeholder": "Tell everyone something about yourself",
                                                        }
                                                ),
                            label="About"                            
                        )
    
    class Meta:

        model = Alumni
        fields = [
            'profile_image',
            'banner_image',
            'field',
            'experience',
            'uni',
            'about'
        ]


class LoginForm(forms.Form):

    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                                      attrs={
                                                                "placeholder":
                                                                "Enter your username"
                                                              }
                                                     )
                               )
    
    password = forms.CharField(max_length=12, 
                               widget=forms.PasswordInput(
                                                        attrs={
                                                                'placeholder':
                                                                "Enter your password"
                                                            }   
                                                        ) 
                                )

      

class StudentForm(forms.ModelForm):
    
    profile_image = forms.ImageField()
    banner_image = forms.ImageField()
    field = forms.CharField(max_length=50, label="Field",
                            widget=forms.TextInput(
                                                   attrs={
                                                         "placeholder":"Your Field"
                                                        }
                                                ))
    uni = forms.CharField(max_length=50, label="University",
                          widget=forms.TextInput(
                                                 attrs={
                                                         "placeholder":"Your University"
                                                        }
                                                ))
    about = forms.CharField(max_length=150, 
                            widget=forms.Textarea(
                                                attrs={
                                                        "placeholder": "Tell everyone something about yourself",
                                                        }
                                                ),
                            label="About"                            
                        )
    
    class Meta:

        model = Student
        fields = [
            'profile_image',
            'banner_image',
            'field',
            'uni',
            'about'
        ]      




