from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def addpost(request):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.email = request.user.email
            newPost.save()

            print('Post Başarıyla Kaydedildi(in terminal)')
            return redirect('index')
    else:
        form = PostForm()
    return render(request,"addpost.html",{"form":form})

def postdetail(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post":post
    }
    return render(request,"postdetail.html",context)