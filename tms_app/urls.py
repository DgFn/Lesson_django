"""
URL configuration for tms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from tms import settings

from tms_app.views.main_view import Main
from tms_app.views.registration import RegistrationView
from tms_app.views.authorization_view import AuthorizationView, user_logout
from tms_app.views.info_user import InfoUserView
from tms_app.views.edit_user_info import EditUserInfoView
from tms_app.views.create_post import PostCreateView

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('authorization/', AuthorizationView.as_view(), name='authorization'),
    path('logout/', user_logout, name='logout'),
    path('info/', InfoUserView.as_view(), name='info'),
    path('edit_info/', EditUserInfoView.as_view(), name='edit_info'),
    path('new_post', PostCreateView.as_view(), name='new_post'),
]
