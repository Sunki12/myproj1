from django.http import HttpResponse

def login(request):
    return HttpResponse("hello login view")