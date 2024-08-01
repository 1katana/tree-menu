from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index/index.html',{'content':0})


def d1(request):
    return render(request,'index/index.html',{'content':1})

def d2(request):
    return render(request,'index/index.html',{'content':2})

def d3(request):
    return render(request,'index/index.html',{'content':3})

def d4(request):
    return render(request,'index/index.html',{'content':4})

def d5(request):
    return render(request,'index/index.html',{'content':6})

def d6(request):
    return render(request,'index/index.html',{'content':6})

def d7(request):
    return render(request,'index/index.html',{'content':7})

def d8(request):
    return render(request,'index/index.html',{'content':8})

def d9(request):
    return render(request,'index/index.html',{'content':9})