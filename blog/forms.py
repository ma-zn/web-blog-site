from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مستخدم بالفعل.")
        return email

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
