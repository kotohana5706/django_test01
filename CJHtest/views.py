from django.shortcuts import render
from .models import Post
from .forms import CommentForm

def post_list(req):
    posts = Post.objects.all()
    return render(req, 'CJHtest/post_list.html', {'posts': posts})
def post(req, page=1):
    page = int(page)
    posts = Post.objects.get(auto_increment_id=page)
    return render(req, 'CJHtest/post.html', {'posts': posts})