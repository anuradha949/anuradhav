from django import forms
from .models import User,Post


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','username']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user','text','created_at','updated_at']
        widgets = {'password':forms.PasswordInput, 'text':forms.Textarea}