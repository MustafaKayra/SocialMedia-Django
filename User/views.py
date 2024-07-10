from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as auth_login,authenticate,logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            password1 = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")

            hashed_password = make_password(password1)

            newUser = User.objects.create(username=username,first_name=first_name,password=hashed_password,email=email)
            auth_login(request,newUser)

            print("Kullanıcı Başarıyla Oluşturuldu")
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request,"register.html")


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                print("Giriş Başarıyla Yapıldı")
                return redirect('index')
            else:
                print("Giriş Yapılamadı")
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request,"login.html",{"form":form})

def logoutuser(request):
    logout(request)
    print("Başarıyla Çıkış Yapıldı")
    return redirect('index')

def UpdateUser(request,id):
    if request.method == "POST":
        user = get_object_or_404(User,id=id)
        form = RegisterForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            password1 = form.cleaned_data.get("password1")

            updated_user = authenticate(username=user.username,password=password1)

            if updated_user is not None:
                auth_login(request,updated_user)
                print("Kullanıcı Başarıyla Güncellendi")
                return redirect('index')
            else:
                print("Büyük Problem!")
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request,"UpdateUser.html")

def deleteuser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    print("Kullanıcı Başarıyla Ortadan Kaldırıldı")
    return redirect('index')