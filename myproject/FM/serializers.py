from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('account','username','password','qq_account','wechat_account')
        # fields = '__all__' 表示最终序列化返回的所有字段