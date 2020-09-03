"""django_practices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import helloworld.views as helloworld_views
import emaillist.views as emaillist_views

urlpatterns = {
    path('hello/', helloworld_views.hello),
    path('hello2/', helloworld_views.hello2),
    path('hello3/', helloworld_views.hello3),

    path('emaillist/', emaillist_views.index),
    path('emaillist/form', emaillist_views.form),

    path('admin/', admin.site.urls),
}
