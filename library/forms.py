from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, EmailInput
from .models import User, Group

class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'password-box', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'password-box', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    class Meta:
        model = User
        fields = ["name", "username", "email"]

        widgets = {
            "name": TextInput(attrs={
                "class": "box-element",
                "placeholder": "Enter Name"
            }),
            "username": TextInput(attrs={
                "class": "box-element",
                "placeholder": "Enter Username" 
            }),
            "email": EmailInput(attrs={
                "class": "box-element",
                "placeholder": "Group Description" 
            }),
        }
class GroupForm(ModelForm):
    class Meta: 
        model = Group
        fields = ["name", "description", "image"]
        
        widgets = {
            "name": TextInput(attrs={
                "class": "box-element",
                "placeholder": "Group Name"
            }),
            "description": TextInput(attrs={
                "class": "box-element",
                "placeholder": "Group Description" 
            }),
        }

class PictureForm(ModelForm):
    class Meta:
        model = User
        fields = ["image"]
