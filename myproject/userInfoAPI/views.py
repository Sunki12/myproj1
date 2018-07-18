from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from userInfoAPI.models import UserInfo
from userInfoAPI.serializers import UserInfoSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the page index.首页")


@api_view(['GET', 'POST'])
def userinfo_list(request):
    global serializer
    if request.method == 'GET':
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def userinfo_show(request):
    if request.method == 'GET':
        req_id = request.GET.get("id")
        #print(req_id)
        userinfo = UserInfo.objects.filter(user_id__exact=req_id)
        seri_info = UserInfoSerializer(userinfo, many= True)
        if userinfo:
            return Response(seri_info.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        # 解析post过来的json数据
        req = json.loads(request.body)
        # 得到相应的参数
        req_id = req.get("id")
        userinfo = UserInfo.objects.filter(user_id__exact=req_id)
        seri_info = UserInfoSerializer(userinfo, many=True)
        if userinfo:
            return Response(seri_info.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def userinfo_change(request):
    if request.method == 'GET':
        req_id = request.GET.get("user_id")
        userinfo = UserInfo.objects.filter(user_id__exact=req_id)#原数据
        sex_2 = request.GET.get("sex")
        userinfo.update(sex=sex_2)
        age_2 = request.GET.get("age")
        userinfo.update(age=age_2)
        height_2 = request.GET.get("height")
        userinfo.update(height=height_2)
        weight_2 = request.GET.get("weight")
        userinfo.update(weight=weight_2)
        district_2 = request.GET.get("district")
        userinfo.update(district=district_2)
        per_taste_2 = request.GET.get("per_taste")
        userinfo.update(per_taste=per_taste_2)
        per_meat_2 = request.GET.get("per_meat")
        userinfo.update(per_meat=per_meat_2)
        per_vege_2 = request.GET.get("per_vege")
        userinfo.update(per_vege=per_vege_2)
        seri_info = UserInfoSerializer(userinfo, many= True)
        return Response(seri_info.data)
    elif request.method == 'POST':
        req = json.loads(request.body)
        req_id = req.get("user_id")
        userinfo = UserInfo.objects.filter(user_id__exact=req_id)#原数据
        sex_2 = req.get("sex")
        userinfo.update(sex=sex_2)
        age_2 = req.get("age")
        userinfo.update(age=age_2)
        height_2 = req.get("height")
        userinfo.update(height=height_2)
        weight_2 = req.get("weight")
        userinfo.update(weight=weight_2)
        district_2 = req.get("district")
        userinfo.update(district=district_2)
        per_taste_2 = req.get("per_taste")
        userinfo.update(per_taste=per_taste_2)
        per_meat_2 = req.get("per_meat")
        userinfo.update(per_meat=per_meat_2)
        per_vege_2 = req.get("per_vege")
        userinfo.update(per_vege=per_vege_2)
        seri_info = UserInfoSerializer(userinfo, many= True)
        return Response(seri_info.data)





