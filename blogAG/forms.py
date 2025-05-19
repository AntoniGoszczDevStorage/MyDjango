from django import forms
from .models import Post
class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znakow')
    class Meta:
        model = Post
        fields = ['image', 'text', 'title']
