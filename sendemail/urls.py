# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

from .views import contactView, successView


urlpatterns = [
    # path('', views.contact.as_view(), name = "contact"),
    path('', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('email/', TemplateView.as_view(template_name='email.html'), name = 'email'),
]