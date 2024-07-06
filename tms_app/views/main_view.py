from django.shortcuts import render
from django.views import View

from tms_app.models import Post


class Main(View):
    """Основная вьюха"""
    def get(self, request):
        """Возвращает основную страницу с постами"""
        posts = Post.objects.all()
        context = {'title': 'Бложик', 'posts': posts}
        return render(request, 'main_page.html', context)


# def commentsview(request):
#     comments = Comment.objects.order_by('id').all()
#     context = {'title': 'Комментики', 'comments': comments}
#     return render(request, 'comment_page.html', context)



