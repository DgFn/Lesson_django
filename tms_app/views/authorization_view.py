from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from tms_app.forms.authorization_form import AuthorizationForm


class AuthorizationView(View):
    """Авторизация"""
    def get(self, request):
        """Возврат форму для ввода данных"""
        form = AuthorizationForm()
        context = {'title': 'Авторизация', 'form': form}
        return render(
            request,
            'authorization_page.html',
            context)

    def post(self, request):
        """Проверка введеных данных и возврат в зависимости от проверки"""

        form = AuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')

        context = {'title': 'Авторизация', 'form': form}
        return render(
            request,
            'authorization_page.html',
            context)

def user_logout(request):
    """Выход пользователя"""
    logout(request)
    return redirect('main')
