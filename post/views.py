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
            author = form.cleaned_data.get("author")
            email = form.cleaned_data.get("email")
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")

            newPost = Post.objects.create(author=author,email=email,title=title,content=content)
            newPost.save()

            print('Post Başarıyla Kaydedildi(in terminal)')
            return redirect('index')
    else:
        form = PostForm()
    return render(request,"addpost.html",{"form":form})
