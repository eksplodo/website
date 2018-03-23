from datetime import datetime

from django.urls import reverse

from users.models import UserProfile
from django.db import models


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(choices=(('skill', '技术文'), ('talk', '杂谈')),max_length=20, verbose_name='类别')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=20, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='作者')
    desc = models.CharField(max_length=100, verbose_name='文章描述', null=True, blank=True)
    image = models.ImageField(upload_to='article/%Y%m', max_length=100, null=True, blank=True, verbose_name='文章刊图')
    content = models.TextField(verbose_name='正文')
    views = models.IntegerField(default=0, verbose_name='浏览数')
    create_time= models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    # 多对多关系
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:rss')