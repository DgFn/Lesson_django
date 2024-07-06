from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View

from tms_app.models import Post, Profile


class InfoUserView(View):
    """Информация о пользователе"""
    def get(self, request, *args, **kwargs):
        """Возвращает страницу с информацией о пользователе"""
        if not request.user.is_authenticated:
            return render(request, 'not_auth.html')
        user_info = User.objects.get(username=request.user)
        profile = Profile.objects.get(user=request.user)
        context = {'title': 'Информация', 'user_info': user_info,'profile': profile}
        return render(request, 'info.html', context)
