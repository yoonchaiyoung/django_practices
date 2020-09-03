from django.shortcuts import render

from emaillist.models import fetchlist

def index(request):
    results = fetchlist()
    data = {'emaillist_list': results}
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')
