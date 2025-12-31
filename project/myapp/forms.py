from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author_name', 'title', 'description', 'image']  # no need for slug
