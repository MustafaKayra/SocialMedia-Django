from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def addpost(request):
    return render(request,"addpost.html")
