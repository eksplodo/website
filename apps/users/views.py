from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import RegisterForm, LoginForm
from utils import send_verify_email

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'register.html', {
                    'register_form': register_form,
                    'msg': '用户已经存在'
                })
            else:
                user_profile = UserProfile()
                password1 = request.POST.get('password1', '')
                password2 = request.POST.get('password2', '')
                email = request.POST.get('email', '')
                if password1 != password2:
                    return render(request, 'register.html', {
                        'register_form': register_form,
                        'msg': '密码不一致'
                    })
                else:
                    user_profile.username = user_name
                    user_profile.password = make_password(password2)
                    user_profile.email = email
                    user_profile.is_active = False
                    user_profile.save()
                    send_verify_email(email, 'register')
                    return HttpResponse('发送成功， 请前往邮箱激活~')
        return render(request, 'register.html')


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                record.delete()
                return HttpResponse('激活成功，请前往登录!')
        else:
            return HttpResponse('激活失败,请检查链接是否失效~')


class LogoutView(View):
    def get(self, request):
        logout(request)
        redirect_to = request.GET.get('next', '')
        return HttpResponseRedirect(redirect_to)



class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_to = request.GET.get('next', '')
                    return HttpResponseRedirect(redirect_to)
                else:
                    return render(request, 'register.html')
            else:
                return render(request, 'index.html')
        else:
            return render(request, 'index.html')