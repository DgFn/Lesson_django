from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View

from tms_app.models import Post


class InfoUserView(View):
    """Информация о пользователе"""
    def get(self, request, *args, **kwargs):
        """Возвращает страницу с информацией о пользователе"""
        user_info = User.objects.get(username=request.user)
        context = {'title': 'Информация', 'user_info': user_info,}
        return render(request, 'info.html', context)
