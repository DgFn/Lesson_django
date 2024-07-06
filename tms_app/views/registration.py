from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from tms_app.forms.registration import RegistrationForm


class RegistrationView(View):
    """Регистрации"""
    def get(self, request):
        """Возвращает форму для регистрации"""
        if request.user.is_authenticated:
            return redirect('main')
        form = RegistrationForm()
        context = {'title': 'Регистрация', 'form': form}
        return render(request, 'registration_form.html', context)

    def post(self, request):
        """Проверяет верно ли введены данные"""

        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        context = {'title': 'Регистрация', 'form': form}
        return render(request, 'registration_form.html', context)
