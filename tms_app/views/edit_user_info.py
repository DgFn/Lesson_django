from django.views import View
from tms_app.forms.edit_form import EditUserInfoForm
from django.shortcuts import redirect, render


class EditUserInfoView(View):
    """Обновление инфы о пользователе"""
    def get(self, request):
        """Возвращает форму для ввода инфы"""
        form = EditUserInfoForm()
        context = {'title': 'Редактирование',
                   'form': form}
        return render(request,
                      'edit_user_info.html',
                      context)

    def post(self, request):
        """Проверяет введеные данные и возвращает страницу в зависимости от данных"""

        form = EditUserInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('info')

        context = {'title': 'Редактирование', 'form': form}
        return render(request, 'edit_user_info.html', context)
