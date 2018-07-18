from django.urls import path

from . import views

app_name = 'userInfoAPI'
urlpatterns = [
    path('', views.index, name='index'),
    path('userinfo_list', views.userinfo_list, name = 'userinfo_list'),
    path('userinfo_show', views.userinfo_show, name = 'userinfo_show'),
    path('userinfo_change', views.userinfo_change, name = 'userinfo_change')

]