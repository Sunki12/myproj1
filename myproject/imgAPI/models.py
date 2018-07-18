from django.db import models

# Create your models here.
from rest_framework.utils import json


class Image(models.Model):
    pic_name = models.CharField(max_length=40)
    #pic_path = models.ImageField(upload_to="pic_folder/", default='pic_folder/None/no_image.pig')
    img_url = models.CharField(max_length=200)



