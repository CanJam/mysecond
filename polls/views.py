from django.shortcuts import render
from django.http import HttpResponse

def index(request): #定义一个方法请求
    return HttpResponse("Hello,world.You're at the polls index.") 
# def nono(request): 自定义
 #   return HttpResponse('nonoo')  
# Create your views here.

