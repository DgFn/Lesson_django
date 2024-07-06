from django import forms
from django.forms import ModelForm

from tms_app.models import Post, PostImage


class CreatePostForm(ModelForm):
    """Форма создания поста"""

    images = forms.ImageField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'name': 'images','type': 'File', 'multiple': True})
        , required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'is_published']

