from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import View

from tms_app.forms.create_post_form import CreatePostForm
from tms_app.models import PostImage


class PostCreateView(View):
    """Новый пост"""

    def get(self, request):
        """Возврат формы для создания поста"""
        form = CreatePostForm()
        return render(request, 'create_page.html', {'form': form})

    def post(self, request):
        """Проверка введеных данных и возврат в зависимости от проверки"""
        if not request.user.is_authenticated:
            return redirect('authorization')
        form = CreatePostForm(request.POST, request.FILES)
        if len(request.FILES.getlist('images')) > 4:
            error_message = 'Незя больше 4 картинок'
            return render(
                request,
                'create_page.html',
                {'form': form, 'error_message': error_message})
        if form.is_valid():

            self.form_valid(form)
            for img in request.FILES.getlist('images'):
                PostImage.objects.create(post=form.instance, image=img)
            return redirect('main')



        return render(
            request,
            'create_page.html',
            {'form': form}, )

    def form_valid(self, form):
        """Устанавливаем текущего пользователя как автора поста"""
        form.instance.user = self.request.user
        form.save()
        return form
