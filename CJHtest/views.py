from django.shortcuts import render
from .models import Post

def post_list(req):
    posts = Post.objects.all()
    return render(req, 'CJHtest/post_list.html', {'posts': posts})
def post(req):
    posts = Post.objects.all()
    return render(req, 'CJHtest/post.html', {'posts': posts})
