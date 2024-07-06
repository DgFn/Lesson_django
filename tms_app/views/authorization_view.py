from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from tms_app.forms.authorization_form import AuthorizationForm


class AuthorizationView(View):
    """Авторизация"""
    def get(self, request):
        """Возврат форму для ввода данных"""
        if request.user.is_authenticated:
            return redirect('main')
        form = AuthorizationForm()
        context = {'title': 'Авторизация', 'form': form}
        return render(
            request,
            'authorization_page.html',
            context)

    def post(self, request):
        """Проверка введеных данных и возврат в зависимости от проверки"""

        error_message = None
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')

            error_message = "Неверный логин или пароль"

        context = {'title': 'Авторизация', 'form': form, 'error_message': error_message}
        return render(
            request,
            'authorization_page.html',
            context)

def user_logout(request):
    """Выход пользователя"""
    logout(request)
    return redirect('main')
