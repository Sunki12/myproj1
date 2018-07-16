from django.urls import path

from . import views
from . import loginviews

app_name = 'FM'
urlpatterns = [
    path('', views.index, name='index'),
    #path('login', loginviews.login, name='login'),
]