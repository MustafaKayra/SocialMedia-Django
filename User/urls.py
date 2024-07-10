from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('updateuser/<int:id>',views.UpdateUser,name="UpdateUser"),
    path('delete/<int:id>',views.deleteuser,name="delete")
]