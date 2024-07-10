from django.contrib import admin
from django.urls import path,include
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Post/',include('post.urls')),
    path('',views.index,name="index"),
    path('about/',views.about,name="about")
]
