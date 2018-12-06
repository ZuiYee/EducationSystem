from django.shortcuts import render, redirect
from .forms import RegisterForm
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
            auth.login(request, re)
            return redirect('/', {'users': re})
        else:
            return render(request, 'users/login.html', {'LoginError': '用户名或密码错误'})
    return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def profile(request):
    return render(request, 'web/profile.html', )


