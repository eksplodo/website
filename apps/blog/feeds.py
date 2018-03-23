from django.contrib.syndication.views import Feed

from .models import Article

class ArticleFeed(Feed):
    title = "eksplodo博客"
    link = "/"
    description = "eksplodo博客RSS"

    def items(self):
        return Article.objects.order_by('-create_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
