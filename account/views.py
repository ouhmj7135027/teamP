from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import (authenticate, login as django_login, logout as django_logout)
from django.contrib.auth.models import User
from .forms import UserForm, LoginForm
from django.views.decorators.csrf import csrf_exempt


def login_page(request):
    if not request.user.is_authenticated:
        data = {"username" : request.user, "is_authenticated" : request.user.is_authenticated}
    else:
        data = {"last_login" : request.user.last_login,
            "username" : request.user.username,
            "password" : request.user.password,
            "is_authenticated" : request.user.is_authenticated,
        }
    return render(request, "account/login_page.html", context={"data" : data})

@csrf_exempt
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        u_id = request.POST.get('u_id')
        pwd = request.POST.get('u_pw')
        user = authenticate(username=u_id, password=pwd)
        if user is not None:
            django_login(request, user)
            request.session['username'] = u_id
            return redirect('/')
        else:
            error = "다시 시도해주세요"
            return render_to_response("account/login_page.html", {"form" : form, "error" : error})
    else:
        error = "큰 ELSE 다시 시도해주세요"
        form = LoginForm()
        return render(request, "account/login_page.html", {"form" : form, "error" : error})

def logout(request):
    django_logout(request)
    return redirect("/") 

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            django_login(request, new_user)
            return redirect("/")
        else:
            context = {"Msg" : "회원가입 실패", "form" : form}
            return render_to_response("account/signup_page.html", context)
    else:
        form = UserForm()
        return render(request, "account/signup_page.html", {"form" : form})


