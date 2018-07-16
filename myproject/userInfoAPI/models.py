from django.db import models
from loginAPI.models import Users


class UserInfo(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    per_taste = models.CharField(max_length=20)
    per_meat = models.CharField(max_length=20)
    per_vege = models.CharField(max_length=20)

    def __str__(self):
        return self.username
