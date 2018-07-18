from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from imgAPI.models import Image
from imgAPI.serializers import ImageSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the page index. ====>imgAPI")


@api_view(['GET', 'POST'])
def showImg(request):
    if request.method == 'GET':
        req_id = request.GET.get("id")
        img_urls = Image.objects.filter(id__exact=req_id)
        seri_url = ImageSerializer(img_urls, many=True)
        #print(seri_url.data)
        if seri_url:
            return Response(seri_url.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        req = json.loads(request.body)
        req_id = req.get("id")
        img_urls = Image.objects.filter(id__exact=req_id)
        seri_url = ImageSerializer(img_urls, many=True)
        if seri_url:
            return Response(seri_url.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
