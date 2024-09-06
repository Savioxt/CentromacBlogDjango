from django.shortcuts import render,HttpResponse
from page.models import Post

def PaginaInicial(request):
    return render(request,'index.html')

def PaginaSobre(request):
    return render(request,'sobre.html')

def PaginaBlog(request):
    posts = Post.objects.all()
    return render(request,'blog.html',{'posts': posts})

def PaginaPost(request, pid):
    post = Post.objects.get(post_id=pid)
    return render(request,'post.html',{'post': post})


