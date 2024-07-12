from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addpost/',views.addpost,name="addpost"),
    path('postdetail/<slug:slug>',views.postdetail,name="postdetail"),
    path('postupdate/<slug:slug>',views.postupdate,name="postupdate"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('postupdate/<slug:slug>',views.postupdate,name="postupdate"),
    path('delete/<slug:slug>',views.deletepost,name="deletepost")
]