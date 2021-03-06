"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import index, post

import rest_framework_jwt.views
import djoser.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', post, name='post'),

    url(r'^auth/login', rest_framework_jwt.views.obtain_jwt_token),  # using JSON web token
    url(r'^auth/register', djoser.views.RegistrationView.as_view()),
    url(r'^auth/password/reset', djoser.views.PasswordResetView.as_view()),
    url(r'^auth/password/reset/confirm', djoser.views.PasswordResetConfirmView.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
