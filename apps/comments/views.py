from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from .models import Comment
from blog.models import  Article

class CommentView(View):
    def post(self, request, art_id):
        article = Article.objects.get(id=art_id)
        comment_text = request.POST.get('comment', '')
        comments = Comment()
        comments.user = request.user
        comments.comment = comment_text
        comments.article = article
        comments.save()
        redirect_to = request.POST.get('next', '')
        return HttpResponseRedirect(redirect_to)
    # else:
    #     return HttpResponse("{'status': 'fail', 'msg': '评论失败'}", content_type='application/json')