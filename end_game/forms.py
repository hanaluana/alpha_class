from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.EmailField()
    class Meta:
        model = Post
        fields = ['title','content']
        # fields = '__all__' 도 가능