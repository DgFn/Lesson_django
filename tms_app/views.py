from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, UserProfile, Comment


# Create your views here.


def main(request):
    posts = Post.objects.prefetch_related('comment_set').all()
    context = {'title': 'Бложик', 'posts': posts}
    return render(request, 'main_page.html', context)


def userprofile(request):
    users = UserProfile.objects.order_by('date_of_birth').all()
    context = {'title': 'Челики', 'users': users}
    return render(request, 'blog_page.html', context)


def commentsview(request):
    comments = Comment.objects.order_by('id').all()
    context = {'title': 'Комментики', 'comments': comments}
    return render(request, 'comment_page.html', context)
