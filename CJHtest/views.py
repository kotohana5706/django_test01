from django.shortcuts import render

def post_list(req):
    return render(req, 'CJHtest/post_list.html', {})