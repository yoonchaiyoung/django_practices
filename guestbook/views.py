from django.http import HttpResponse
from django.shortcuts import render

import guestbook.models as guestbookmodel


def index(request):
    # return HttpResponse('<h1>Hello World</h1>', content_type='text/html')
    results = guestbookmodel.fetchlist()
    data = {'guestbooklist': results}
    return render(request, 'guestbook/index.html', data)


def add(request):
    print(request.POST)
    return HttpResponse('ok', content_type='text/html')
