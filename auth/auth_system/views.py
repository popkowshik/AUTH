from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def Homepage(request):
    return render(request, 'files/index.html', {})

def Register(request):

    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("sname")
        uname = request.POST.get("uname")
        mail = request.POST.get("mail")
        passw = request.POST.get("passw")

        new_user = User.objects.create_user(uname, mail, passw)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect("login-page")
    
    return render(request, 'files/register.html', {})

def Login(request):

    if request.method == "POST":
        uname = request.POST.get("uname")
        passw = request.POST.get("pass")

        user = authenticate(request, username=uname, password=passw)

        if user is not None:
            return HttpResponse("ERROR ! user does not exist")

        else:
            login(request, user)
            return redirect("home-page")
            

    return render(request, 'files/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect("login-page")