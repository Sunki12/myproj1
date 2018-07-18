from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        ##fields = '__all__'
        fields = ('img_url',)
        # fields = '__all__' 表示最终序列化返回的所有字段