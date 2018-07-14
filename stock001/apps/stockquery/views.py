from django.http import HttpResponse
from django.http import HttpResponseRedirect
import django.http as http
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.stockquery.models import user
import pandas as pd
from django.db import connection
from django.contrib import messages
from sqlalchemy import create_engine
import tushare as ts
import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import numpy as np
import random
import datetime
from .forms import ImgForm
import json


# Create your views here.
def stockquery(request):
    #return HttpResponse("Hello world ! ")
    return render(request, 'stockquery.html')
    #return HttpResponseRedirect('http://stockpage.10jqka.com.cn/600160/')


def gotostock(request):
    stockname = request.GET.get('stock')
    if len(stockname) == 6:
    #return render(request, 'stockquery.html')
        return HttpResponseRedirect('http://stockpage.10jqka.com.cn/'+stockname+'/')
    else:
        return HttpResponse("Please input the right stock number!")

def qushitu(request):
    stockname = request.GET.get('stock2')
    df=ts.get_k_data('002743',start='2018-05-01')
    #messages.add_message(request, messages.INFO, df.iloc[1:2,1:2].values)
    messages.add_message(request, messages.INFO, df.values[0,2])
    return render(request, 'messageshow.html')


def gen_mat(request):
    fig=Figure(figsize=(6,6))
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvasAgg(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    fig.savefig('static/images/002.jpg')
    form = ImgForm('/images/002.jpg')
    #plt.close(fig)
    #return response
    #messages.add_message(request, messages.INFO, response)
    #return render(request, 'messageshow.html')
    return render(request,'messageshow.html',{'images':'images/002.jpg'})
    #return render(request, 'messageshow.html', {'form':form})

def read_data(request):
    dd = user.objects.raw('select * from stockquery_user')
    #return HttpResponse('hhhhhh')
    #messages.success(request,'Hello what?')
    for mm in dd:
        messages.add_message(request, messages.INFO, mm.username)
        messages.add_message(request, messages.INFO, mm.chiname)
    messages.add_message(request, messages.INFO, dd[0].username)
    return render(request, 'messageshow.html')


def read_data2(request):
    cursor = connection.cursor()
    cursor.execute("select * from stockquery_user")
    row = cursor.fetchone()
    #rr = cursor.execute("delete from stockquery_user where username='zhuzhu'")


#sqlalchemy read
def read_data3(request):
    engine = create_engine('mysql://root:julian88@localhost/dbstock')
    df = pd.read_sql("select * from stockquery_user",con= engine)
    messages.add_message(request, messages.INFO, df.ix[0,4])
    return render(request, 'messageshow.html')

def add(request):
    context = {}
    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = int(a) + int(b)
        context['result'] = c
        return HttpResponse(json.dumps({'result':c,}), content_type="application/json")

def read_stock(request):
    context = {}
    if request.method == 'GET':
        engine = create_engine('mysql://root:julian88@localhost/dbstock')
        df = pd.read_sql("select date,open,close,high,low,volume,code from stick_data", con=engine)
        res2 = df.values.tolist()   #dataframe格式先转化成list
        res = user.objects.values('username', 'chiname', 'phnum', 'email')
        res3 = list(res)
        #print(type(res), type(res2))
        #res2 = list(res)   #非常重要，需要先list化，才可以转化成json
        #data = {'username':res.iloc[0,1], 'chiname':res.iloc[0,2]}
        return HttpResponse(json.dumps({'result': res2,}), content_type="application/json")
        #return HttpResponse(request,data)

def insdata(request):
    engine = create_engine('mysql://root:julian88@localhost/dbstock')
    #df = ts.get_k_data('601288', index=True, start='20180101', end='20180711')
    df = ts.get_k_data('601288')
    df.to_sql('stick_data', engine)
    return HttpResponse("insert sucessful")