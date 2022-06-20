from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostCreateForm
# Create your views here.
def index (request):
    posts=Post.objects.all().filter(status='pub')
    context={'posts': posts}
    return render (request, 'blog/index.html',context)


def PostDetail (request ,id):
    try:
        post=Post.objects.get(id=id)
        context={'post':post}
        return render (request, 'blog/detail.html',context)
    except:
        return render (request, 'admin/404.html')


def CreatePost (request):
    context={}
    if request.method == 'POST':
       form=PostCreateForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('blog_index')   
    else: 
        form=PostCreateForm()
        context['form']=form
        return render (request, 'blog/create_form.html', context)
    
