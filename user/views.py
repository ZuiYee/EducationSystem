from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import RegisterForm, UserForm
from django.contrib.auth.models import User
from django.contrib import auth



def regist(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST) #包含用户名和密码
        if form.is_valid():
            #获取表单数据
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/regist.html', context={'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re = auth.authenticate(username=username, password=password)
        if re is not None:
            identity = request.POST.get('identity')
            if identity:
                if re.identity == identity:
                    auth.login(request, re)
                    if request.POST.get('identity') == '学生':
                        return redirect(reverse('web:studentProfile'))
                    else:
                        return redirect(reverse('web:teacherProfile'))
                else:
                    return render(request, 'users/login.html', {'LoginError': '身份选择错误'})
            else:
                return render(request, 'users/login.html', {'LoginError': '请选择身份'})
        else:
            return render(request, 'users/login.html', {'LoginError': '用户名或密码错误'})
    return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')




def teacherchange(request):
    if request.method == 'GET':
        form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'web/teacherparseresult.html', context={'Print': '更改信息已保存!'})

    context = {'form': form}
    return render(request, 'users/teacherchange.html', context)

def studentchange(request):
    if request.method == 'GET':
        form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'web/studentparseresult.html', context={'Print': '更改信息已保存!'})
    return render(request, 'users/studentchange.html', context={'form': form})

def studentchangepassword(request):
    if request.method == 'GET':
        form = RegisterForm(instance=request.user)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'web/studentparseresult.html', context={'Print': '更改密码已保存!'})
    return render(request, 'users/studentchangepassword.html', context={'form': form})

def teacherchangepassword(request):
    if request.method == 'GET':
        form = RegisterForm(instance=request.user)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'web/teacherparseresult.html', context={'Print': '更改密码已保存!'})
    return render(request, 'users/teacherchangepassword.html', context={'form': form})