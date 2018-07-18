from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path

from . import views

app_name = 'imgAPI'
urlpatterns = [
                  path('', views.index, name='index'),
                  path('showImg', views.showImg, name='showImg'),

              ]
