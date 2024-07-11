from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addpost/',views.addpost,name="addpost"),
    path('postdetail/<slug:slug>',views.postdetail,name="postdetail")
]