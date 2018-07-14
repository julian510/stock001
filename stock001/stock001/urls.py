"""stock001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from . import view
from apps.stockquery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', view.welcome),
    path('', views.stockquery),
    path('logon/',view.logon),
    path('dbtest/',view.dbtest),
    path('newuser/', view.new_user),
    path('newuser_action/', view.new_user_action),
    path('query/',views.stockquery),
    path('query/gotostock/',views.gotostock),
    path('qushitu/', views.qushitu),
    path('test/',views.read_data),
    path('test2/',views.read_data2),
    path('test3/',views.read_data3),
    path('gen_mat/', views.gen_mat),
    path('add/',views.add),
    path('read_stock/', views.read_stock),
    path('insdata/', views.insdata),

]