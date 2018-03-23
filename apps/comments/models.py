from datetime import datetime
from django.db import models

from users.models import UserProfile
from blog.models import Article

class Comment(models.Model):
    """
    评论系统
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    comment = models.CharField(max_length=500, verbose_name='评论')
    # auto_now_add 的作用是，当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间。
    created_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
