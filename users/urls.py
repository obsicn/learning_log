"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    # Login page
    # url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^login/$', login, {'template_name': 'users/login.html', 'authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    # Registration page
    url(r'^register/$', views.register, name='register'),
]