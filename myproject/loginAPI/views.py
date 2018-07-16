from django.http import HttpResponse, HttpResponseRedirect, response
from django.shortcuts import render, render_to_response

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Users
from .serializers import UserSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the page index.")


@api_view(['GET', 'POST'])
def user_list(request):
    global serializer
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def regist(request):
    if request.method == 'POST':
        req = json.load(request.body)
        username = req.get("username")
        password = req.get("password")
        data = request.data
        # 向数据库中写入数据
        Users.objects.create(username=username, password=password)
        serializer = UserSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(username,password)

    elif request.method == 'GET':
        # 获取GET方法中的username password参数
        username = request.GET.get("username")
        password = request.GET.get("password")
        # print(username,password)
        Users.objects.create(username=username, password=password)
        # print("get method")
        return Response(status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        #解析post过来的json数据
        req = json.loads(request.body)
        #得到相应的参数
        username = req.get("username")
        password = req.get("password")
        #print(username,password)
        user = Users.objects.filter(username__exact=username, password__exact=password)
        if user:
            return Response(status.HTTP_202_ACCEPTED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        username = request.GET.get("username")
        password = request.GET.get("password")
        user = Users.objects.filter(username__exact=username, password__exact=password)
        if user:
            #return HttpResponseRedirect('/loginAPI/users')
            return Response(status.HTTP_202_ACCEPTED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
