
# Create your models here.
from datetime import timezone, datetime

from django.db import models

class Users(models.Model):
    account = models.CharField(max_length=11)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    is_bound_qq = models.BooleanField(default=False)
    is_bound_wechat = models.BooleanField(default=False)
    qq_account = models.CharField(max_length=20,default=None)
    wechat_account = models.CharField(max_length=20,default=None)

    def __str__(self):
        return self.username
