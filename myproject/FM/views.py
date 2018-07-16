from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from .models import Users
from .serializers import UserSerializer

'''
class JSONResponse(HttpResponse):
    def __init__(self, data, **kw):
        content = JSONRenderer().render(data)
        kw['content_type'] = 'application/json'
        content = '{"Users":' + content + '}'
        super(JSONResponse,self).__init__(content, **kw)
'''

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'FM/login.html')
'''
def user_account(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users)
        #return JSONResponse(serializer.data)


@api_view(['GET','POST'])
def getusers(request, format =None):
    if request.method =='GET':
        users = Users.objects.all()
'''

