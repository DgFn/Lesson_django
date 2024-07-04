from django.shortcuts import render, redirect
from django.views.generic import CreateView

from tms_app.forms.create_post_form import CreatePostForm


class PostCreateView(CreateView):
    """Новый пост"""

    def get(self, request):
        """Возврат формы для создания поста"""
        form = CreatePostForm()
        return render(request, 'create_page.html', {'form': form})

    def post(self, request):
        """Проверка введеных данных и возврат в зависимости от проверки"""
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)

        return render(request, 'create_page.html', {'form': form})

    def form_valid(self, form):
        """Устанавливаем текущего пользователя как автора поста"""
        form.instance.user = self.request.user
        form.save()
        return redirect('main')
