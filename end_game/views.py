from django.shortcuts import render
from .models import Post
from .forms import PostForm


# Create your views here.
def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
