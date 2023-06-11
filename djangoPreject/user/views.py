from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm

@login_required(login_url='/login/')
def index(request):
    return render(request, 'user/login.html')

def Login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('system:index')
            else:
                return HttpResponse("账号或密码输入有误。请重新输入～")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'user/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")

def Register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password1'])
            new_user.save()
            return redirect("user:login")
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'user/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")

def Logout(request):
    logout(request)
    return render(request, 'user/login.html')

@login_required(login_url='/login/')
def Delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('user:login')
        else:
            return HttpResponse('你没有删除操作的权限。')
    else:
        return HttpResponse("仅接受post请求。")