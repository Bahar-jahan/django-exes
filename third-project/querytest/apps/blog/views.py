from django.shortcuts import render
from .models import *
# Create your views here.

def index (request):
    try:
        posts=Post.objects.all()
        context={'posts': posts}
        return render(request, 'blog/index.html', context)
    except: 
        return render(request, 'blog/notfound.html')


def PostView(request , id ):
    try:
        post =Post.objects.get(id=id)
        context={'post': post}
        return render(request, 'blog/details.html', context)

    except: 
        
        context={'post': {'title': 'post not found ' , 'description': '.........'}}
        return render(request, 'blog/details.html', context)
