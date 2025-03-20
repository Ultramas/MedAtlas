"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

#from showcase.api import ChatterBotView
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
#from sendemail.views import contactView, successView

from django.contrib.auth import views as auth_views #import this
from . import views


from showcase import urls as showcase_urls

from rest_framework import routers
router = routers.DefaultRouter()


app_name = "main"

urlpatterns = [
    
    path('admin/', admin.site.urls),  

    path('accounts/', include('django.contrib.auth.urls')),  
    
    path('', include('showcase.urls')),

    re_path(r'^api/', include(router.urls)),
    #re_path(r'^api/chatterbot/', ChatterBotView.as_view(), name='chatterbot'),
    #re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #path('accounts/', include('django.contrib.auth.urls'))

     #path('accounts/', include('django.contrib.auth.urls')),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),      

    #path("password_reset", views.password_reset_request, name="password_reset"),
                                        
                                         # new
    
    #path('contact/', contactView, name='contact'),

    #path('success/', successView, name='success'),


        # Change Password
    # Forget Password
   # Change Password
# path('change-password/', auth_views.PasswordChangeView.as_view(
#            template_name='registration/change-password.html',
#            success_url = '/'
#        ),
#        name='change_password'
#    ),
       
# path('password-reset/',
#         auth_views.PasswordResetView.as_view(
#             template_name='templates/password-reset/password_reset.html',
#             subject_template_name='templates/password-reset/password_reset_subject.txt',
#             email_template_name='registration/password-reset/password_reset_email.html',
#             success_url='/login/'
#         ),
#         name='password_reset'),
#    path('password-reset/done/',
#         auth_views.PasswordResetDoneView.as_view(
#             template_name='registration/password-reset/password_reset_done.html'
#         ),
#         name='password_reset_done'),
#    path('password-reset-confirm/<uidb64>/<token>/',
#         auth_views.PasswordResetConfirmView.as_view(
#             template_name='registration/password-reset/password_reset_confirm.html'
#         ),
#         name='password_reset_confirm'),
#    path('password-reset-complete/',
#         auth_views.PasswordResetCompleteView.as_view(
#             template_name='registration/password-reset/password_reset_complete.html'
#         ),
#         name='password_reset_complete'),

#    path('password_reset_form/',
#         auth_views.PasswordResetCompleteView.as_view(
#             template_name='registration/password_reset_form.html'
#         ),
#         name='password_reset_form'),

    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='commons/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
             success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)