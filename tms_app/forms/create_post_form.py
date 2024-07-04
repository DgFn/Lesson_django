from django.forms import ModelForm

from tms_app.models import Post


class CreatePostForm(ModelForm):
    """Форма создания поста"""
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_published', 'image']
