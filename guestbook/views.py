from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import guestbook.models as guestbookmodel


def index(request):
    # return HttpResponse('<h1>Hello World</h1>', content_type='text/html')
    results = guestbookmodel.fetchlist()
    data = {'guestbooklist': results}
    return render(request, 'guestbook/index.html', data)


def add(request):
    print(request.POST)
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    guestbookmodel.insert(name, password, message)

    return HttpResponseRedirect('/guestbook')



def deleteform(request):
    return render(request, 'guestbook/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    guestbookmodel.delete(no, password)
    return HttpResponseRedirect('/guestbook')


