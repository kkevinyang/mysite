from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        # 当user_login被一个GET请求（request）调用，我们实例化一个新的登录表单（form）
        # 并通过form = LoginForm(),在模板（template）中展示它
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    """
    login_required:
    如果用户没有通过认证，它会把用户重定向到带有一个名为next的GET参数的登录URL，
    该GET参数保存的变量为用户当前尝试访问的页面URL。
    通过这些动作，登录视图（view）会将登录成功的用户重定向到用户登录之前尝试访问过的URL。
    我们在登录模板（template）中的登录表单（form）中添加的隐藏<input>就是为了这个目的。

    section:
    定义了一个section变量。我们会使用该变量来跟踪用户在站点中正在查看的页面。
    多个视图（views）可能会对应相同的section。这是一个简单的方法用来定义每个视图（view）对应的section
    """
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

