import xadmin

from .models import Article, Category, Tag


class ArticleAdmin(object):
    list_display = ['title', 'author', 'views', 'create_time', 'modify_time', 'category', 'tag']
    list_filter = ['title', 'author', 'views', 'category', 'tag']
    search_fields = ['title', 'author', 'views', 'category', 'tag']

class CategoryAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

class TagAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)