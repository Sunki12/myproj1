from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        #fields = ('username','password')
        # fields = '__all__' 表示最终序列化返回的所有字段