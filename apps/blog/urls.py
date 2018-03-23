from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .feeds import ArticleFeed
from .views import IndexView, DetailView, CategoryView

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<int:art_id>/', DetailView.as_view(), name='article'),
    path('category/<str:cat>/', CategoryView.as_view(), name='category'),
    path('rss', ArticleFeed(), name='rss'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)