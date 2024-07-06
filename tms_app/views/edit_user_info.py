from django.views import View
from tms_app.forms.edit_form import EditUserInfoForm, EditProfileForm
from django.shortcuts import redirect, render


class EditUserInfoView(View):
    """Обновление инфы о пользователе"""

    def get(self, request):
        """Возвращает форму для ввода инфы"""

        if not request.user.is_authenticated:
            return render(request, 'not_auth.html')

        form = EditUserInfoForm()
        form_profile = EditProfileForm()
        context = {'title': 'Редактирование',
                   'form': form, 'form_profile': form_profile}
        return render(request,
                      'edit_user_info.html',
                      context)

    def post(self, request):
        """Проверяет введеные данные и возвращает страницу в зависимости от данных"""

        form = EditUserInfoForm(request.POST, instance=request.user)
        form_profile = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and form_profile.is_valid():
            form.save()
            form_profile.save()
            return redirect('info')

        context = {'title': 'Редактирование', 'form': form, 'form_profile': form}
        return render(request, 'edit_user_info.html', context)
