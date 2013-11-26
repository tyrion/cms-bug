from django.http import HttpResponse

def index(request):
    return HttpResponse('index')

def bug(request):
    return HttpResponse('bug')
