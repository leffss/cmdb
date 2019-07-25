from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import User, LoginLog
from .forms import LoginForm, ChangePasswdForm
from util.tool import login_required, hash_code, post_required
import time
# Create your views here.


def login_event_log(user, event_type, detail, address, useragent):
    event = LoginLog()
    event.user = user
    event.event_type = event_type
    event.detail = detail
    event.address = address
    event.useragent = useragent
    event.save()


def login(request):
    if request.session.get('islogin', None):  # 不允许重复登录
        return redirect(reverse('assets:index'))
    if request.method == "POST":        
        login_form = LoginForm(request.POST)
        error_message = '请检查填写的内容!'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
                if user.status == 1:
                    error_message = '用户已禁用!'                    
                    login_event_log(user, 3, '用户 {} 已禁用'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
                    return render(request, 'login/login.html', locals())
            except BaseException:
                error_message = '用户不存在!'                
                login_event_log(None, 3, '用户 {} 不存在'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
                return render(request, 'login/login.html', locals())
            if user.password == hash_code(password):
                request.session.set_expiry(0)
                request.session['islogin'] = True
                request.session['userid'] = user.id
                request.session['username'] = user.username
                request.session['nickname'] = user.nickname
                now = int(time.time())
                request.session['logintime'] = now
                request.session['lasttime'] = now                
                login_event_log(user, 1, '用户 {} 登陆成功'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
                return redirect(reverse('assets:index'))
            else:
                error_message = '密码错误!'
                login_event_log(user, 3, '用户 {} 密码错误'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
                return render(request, 'login/login.html', locals())
        else:
            login_event_log(None, 3, '登陆表单验证错误', request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
            return render(request, 'login/login.html', locals())
    return render(request, 'login/login.html')


def logout(request):
    if not request.session.get('islogin', None):
        return redirect(reverse('login:login'))
    user = User.objects.get(id=int(request.session.get('userid')))
    request.session.flush()     # 清除所有后包括django-admin登陆状态也会被清除
    # 或者使用下面的方法
    # del request.session['islogin']
    # del request.session['userid']
    # del request.session['username']
    login_event_log(user, 2, '用户 {} 退出'.format(user.username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
    return redirect(reverse('login:login'))


@login_required
@post_required
def change_passwd(request):
    changepasswd_form = ChangePasswdForm(request.POST)
    if changepasswd_form.is_valid():
        username = request.session.get('username')
        oldpassword = changepasswd_form.cleaned_data.get('oldpasswd')
        newpasswd = changepasswd_form.cleaned_data.get('newpasswd')
        newpasswdagain = changepasswd_form.cleaned_data.get('newpasswdagain')
        try:
            user = User.objects.get(username=username)
            if user.status == 1:
                error_message = '用户已禁用!'
                login_event_log(user, 4, '用户 {} 已禁用'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
                return JsonResponse({"code": 401, "err": error_message})
            if newpasswd != newpasswdagain:
                error_message = '两次输入的新密码不一致'
                login_event_log(user, 4, '两次输入的新密码不一致', request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
                return JsonResponse({"code": 400, "err": error_message})
        except BaseException:
            error_message = '用户不存在!'
            login_event_log(None, 4, '用户 {} 不存在'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
            return JsonResponse({"code": 403, "err": error_message})
        if user.password == hash_code(oldpassword):
            data = {'password': hash_code(newpasswd)}
            User.objects.filter(username=username).update(**data)
            login_event_log(user, 5, '用户 {} 修改密码成功'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
            return JsonResponse({"code": 200, "err": ""})
        else:
            error_message = '当前密码错误!'
            login_event_log(user, 4, '用户 {} 当前密码错误'.format(username), request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
            return JsonResponse({"code": 404, "err": error_message})
    else:
        error_message = '请检查填写的内容!'
        user = User.objects.get(username=request.session.get('username'))
        login_event_log(user, 4, '修改密码表单验证错误', request.META.get('REMOTE_ADDR', None), request.META.get('HTTP_USER_AGENT', None))
        return JsonResponse({"code": 406, "err": error_message})


@login_required
def user_info(request):
    username = request.session.get('username')
    user = User.objects.filter(username=username).values('id', 'username', 'nickname', 'email', 'sex', 'status', 'create_time')
    user_info = dict(user[0])
    user_info['create_time'] = user[0]['create_time'].strftime('%Y/%m/%d %H:%M:%S')
    return JsonResponse({"code": 200, "user": user_info})

