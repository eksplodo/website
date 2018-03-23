import markdown

from pure_pagination import PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View

from .models import Article, Tag, Category
from comments.models import Comment


class IndexView(View):
    def get(self, request):
        current_page = 'home'
        article_list = Article.objects.all().order_by('-create_time')
        hot_articles = Article.objects.all().order_by('-views')[:5]
        tag_list = Tag.objects.all()[:5]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_list, 3, request=request)

        article_list = p.page(page)

        return render(request, 'index.html', {
            'article_list': article_list,
            'tag_list': tag_list,
            'hot_articles': hot_articles,
            'current_page': current_page
        })


class DetailView(View):
    def get(self, request, art_id):
        article = Article.objects.get(id=art_id)
        article.views += 1
        article.save()
        comments = Comment.objects.filter(article=article).order_by('-created_time')
        # 评论数量
        comments_nums = article.comment_set.count()
        related_list = Article.objects.filter(category__name=article.category.name)[:5]
        hot_articles = Article.objects.all().order_by('-views')[:5]
        article.content = markdown.markdown(article.content,
                                            extensions=[
                                                'markdown.extensions.extra',
                                                'markdown.extensions.codehilite',
                                                'markdown.extensions.toc',
                                            ])

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(comments, 3, request=request)

        comments = p.page(page)

        return render(request, 'article.html', {
            'article': article,
            'hot_articles': hot_articles,
            'comments': comments,
            'comments_nums': comments_nums,
            'related_list': related_list,
        })


class CategoryView(View):
    def get(self, request, cat):
        hot_articles = Article.objects.all().order_by('-views')[:5]
        if cat == 'skill':
            current_page = 'skill'
            article_list = Article.objects.filter(category__name=cat)
            return render(request, 'category.html', {
                'article_list': article_list,
                'hot_articles': hot_articles,
                'category': '授人以渔',
                'current_page': current_page,
            })
        elif cat == 'talk':
            current_page = 'talk'
            article_list = Article.objects.filter(category__name=cat)
            return render(request, 'category.html', {
                'article_list': article_list,
                'hot_articles': hot_articles,
                'category': '生活随笔',
                'current_page': current_page,
            })


"""
Article.objects.filter(category=category)
"""