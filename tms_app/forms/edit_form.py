from django.contrib.auth.models import User
from django.forms import ModelForm

from tms_app.models import Profile


class EditUserInfoForm(ModelForm):
    """Форма изменения информации о пользователе"""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(ModelForm):
    """Форма для редактирования профиля пользователя"""

    class Meta:
        model = Profile
        fields = ['profile_pic', 'phone_number', 'github_link']
