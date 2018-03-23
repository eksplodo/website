from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """
    用户资料
    """
    nickname = models.CharField(max_length=50, verbose_name='姓名')
    birthday = models.DateTimeField(default=datetime.now, verbose_name='生日')
    gender = models.CharField(choices=(('female', '女'), ('male', '男')), default='male', verbose_name='性别', max_length=30)
    avatar = models.ImageField(upload_to='avatar/%Y%m', verbose_name='头像')

    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')),
                                 default='register', verbose_name='类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}'.format(self.email)