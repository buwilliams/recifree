from django.urls import path

from . import views


urlpatterns = [
    path('', views.redirect_user, name='redirect'),
    path('login', views.login_form, name='login_form'),
    path('login_process', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup_form, name='signup_form'),
    path('signup_process', views.signup_user, name='signup'),
]
