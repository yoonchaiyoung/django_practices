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

import helloworld.views as helloworldviews
import emaillist.views as emaillistviews
import guestbook.views as guestbookviews



urlpatterns = {
    path('hello/', helloworldviews.hello),
    path('hello2/', helloworldviews.hello2),
    path('hello3/', helloworldviews.hello3),

    path('emaillist/', emaillistviews.index),
    path('emaillist/form', emaillistviews.form),
    path('emaillist/add', emaillistviews.add),

    path('guestbook/', guestbookviews.index),
    path('guestbook/add', guestbookviews.add),
    path('guestbook/deleteform', guestbookviews.deleteform),
    path('guestbook/delete', guestbookviews.delete),

    path('admin/', admin.site.urls),
}
