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

def postupdate(request,slug):
    if request.method == "POST":
        post = Post.objects.get(slug=slug)
        form = PostForm(request.POST or None,instance=post)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            print("Gönderi Başarıyla Güncellendi")

            return redirect('index')
        else:
            print("Formda Hata Yapıldı!")
    else:
        form = PostForm()
    return render(request,"postupdate.html",{"form":form})

def deletepost(request,slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    print("Gönderi Başarıyla Silindi")
    return redirect('index')

def dashboard(request):
    posts = Post.objects.filter(author = request.user)
    context = {
        "posts":posts
    }
    return render(request,"dashboard.html",context)