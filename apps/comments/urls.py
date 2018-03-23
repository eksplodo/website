from django.urls import path

from .views import CommentView

app_name = 'comments'
urlpatterns = [
    path('<int:art_id>/', CommentView.as_view(), name='comment')
]