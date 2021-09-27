from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect




# Create your views here.
def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        email=form.cleaned_data.get("email")
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        login(request, user)
        messages.info(request, "Your account has been created successfully")
        return redirect("home")
    return render(request, "register.html", {"form":form})

def loginUser(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=(authenticate(username=username, password=password))
        if user is None:
            messages.info(request, "Not found...")
            return render(request, "login.html", {"form":form})
        login(request,user)
        messages.info(request, "You logged successfully")
        return redirect("home")
    return render(request, "login.html", {"form":form})

def logoutUser(request):
    logout(request)
    return redirect("home")

