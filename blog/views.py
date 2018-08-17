from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_lists(request):
    posts = Post.objects.filter(author=Amethyst).order_by('published date')
    return render(request, 'blog/post_list.html', {'posts': posts})


