from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        # fields = '__all__' 表示最终序列化返回所有字段