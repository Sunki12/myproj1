from django.urls import path

from . import views

app_name = 'loginAPI'
urlpatterns = [
    path('', views.index, name='index'),
    #path('login', loginviews.login, name='login'),
    path('users', views.user_list ,name = 'user_list'),
    path('regist', views.regist, name = 'regist'),
    path('login', views.login, name = 'login')
]