from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from emaillist.models import fetchlist, insert


def index(request):
    results = fetchlist()
    data = {'emaillist_list': results}
    return render(request, 'emaillist/index.html', data)


def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    first_name = request.POST['fn']
    last_name = request.POST['ln']
    email = request.POST['email']

    insert(first_name, last_name, email)

    return HttpResponseRedirect('/emaillist')