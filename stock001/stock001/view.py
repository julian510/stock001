from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.stockquery.models import user
from django import forms
from django.db import connection

def dbtest(request):
    #return HttpResponse("Hello world ! ")
    test = user(nameid='000001', chiname='tuzhi', enname='julian', phnum='18918378702', passwd='111111')
    test.save()
    return HttpResponse("添加数据成功！")

def dblist(request):
    user_list = user.objects.all()
    return render(request, 'dblist.html', {'user_list': user_list})

def welcome(request):
    return render(request, 'logon.html')

@csrf_exempt
def logon(request):
    if request.method == 'GET':
        name = request.GET.get('username')
        pwd = request.GET.get('password')
        return HttpResponse('get work')
    elif request.method == 'POST':
        name1 = request.POST.get('username')
        pwd = request.POST.get('password')
        if user.objects.filter(username=name1, passwd=pwd).exists():
            return HttpResponseRedirect('/query/')
        else:
            return HttpResponse('wrong')
    else:
        return HttpResponse('wrong')


def new_user(request):
    return render(request,'newuser.html')


@csrf_exempt
def new_user_action(request):
    if request.method == 'POST':
        ename = request.POST.get('ename')
        pwd = request.POST.get('password')
        chiname = request.POST.get('chiname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
    #insertuser = user(username=ename, passwd=pwd, chiname=chiname, phnum=phone, email=email)
    #insertuser.save()
    #return HttpResponse("新增用户成功！")
    cursor = connection.cursor()
    str = "insert into stockquery_user VALUES(username="'+ename+'",passwd="'pwd'", chiname="'chiname'", phnum="'phone'", email="'email'")"
    str2 = "insert into stockquery_user VALUES(username='ename'"
    result = cursor.execute(str)
    #result = cursor.execute('insert into stockquery_user VALUES(username=%s,passwd=%s, chiname=%s, phnum=%s, email=%s)',[ename],[pwd],[chiname],[phone],[email])
    if result == 1:
        return HttpResponse("新增用户成功！")
