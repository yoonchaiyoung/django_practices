from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('<h1>Hello World</h1>', content_type='text/html')
    return render(request, 'guestbook/index.html')