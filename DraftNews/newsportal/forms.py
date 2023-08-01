from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class NewsForm(forms.ModelForm):
    post_body = forms.CharField(min_length=50, label='Содержание')
    post_title = forms.CharField(min_length=10, max_length=64, label='Заголовок')

    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_body',
            'categories',
            'author'
        ]
        labels = {
            'author': 'Автор',
            'categories': 'Темы'
        }