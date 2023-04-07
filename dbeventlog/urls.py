"""eventlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from dbeventlogapp import views
from django.contrib.auth import views as auth_views

admin.site.site_header = "Sinch SDI DB Admin"
admin.site.site_title = "DB Admin"
admin.site.index_title = "Sinch"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('add_event/', views.add_event, name="add_event"),
    path('list_event/', views.list_event, name='list_event'),
    path('add_server/', views.add_server, name='add_server'),
    path('list_server/', views.list_server, name='list_server'),
    path('add_site/', views.add_site, name='add_site'),
    path('list_site/', views.list_site, name='list_site'),
    path('delete_server/<str:pk>/', views.delete_server, name="delete_server"),
    path('update_server/<str:pk>/', views.update_server, name="update_server"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("change-password/", auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html") , name='password_change'),
    path("change-password/done/", auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html") , name='password_change_done'),
    path("password-reset", auth_views.PasswordResetView.as_view( template_name="registration/password_reset_form.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view( template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view( template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view( template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
]
