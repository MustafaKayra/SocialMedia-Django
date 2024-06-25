from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def addtweet(request):
    return render(request,"addtweet.html")
