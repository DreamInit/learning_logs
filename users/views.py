from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """log out user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """register new user"""
    if request.method != 'POST':
        # 显示空的 注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表格
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
