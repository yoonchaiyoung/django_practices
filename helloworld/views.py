from django.shortcuts import render

def hello(request):
    return render(request, 'helloworld/hello.html')

def hello2(request):
    return render(request, 'helloworld/hello2.html')

def hello3(request):
    name = request.GET['name']
    data = {'n': name}
    return render(request, 'helloworld/hello3.html', data)