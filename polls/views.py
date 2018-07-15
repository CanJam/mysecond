#！-*-coding：UTF-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question
"""
#问题：页面的设计写死在视图函数的代码里的
def index(request): #定义一个方法请求
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

#优化1：在templates 目录建立独立的 index.html将页面的设计从代码中分离出来
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }   
    return HttpResponse(template.render(context,request))
"""    
#使用快捷函数render()(请求对象,模板名,字典作为可选)函数将请求对象的参数返回给定的上下文所呈现的给定模板的HttpResponse对象
#The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.
#It returns an HttpResponse object of the given template rendered with the given context.
#优化2：使用render()方法   
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }  
    return render(request,'polls/index.html',context)
# def nono(request): 自定义
 #   return HttpResponse('nonoo')  
def detail(request, question_id): #detail(request=<HttpRequest object>, question_id=34)调用形式
    return HttpResponse("You're looking at question %s." % question_id)
#优化1：引入404异常，如果指定问题 ID 所对应的问题不存在，这个视图就会抛出一个 Http404 异常
#使用（try: except raise） 一般抛异常都是用try
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})        
def results(request, question_id):    
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    
# Create your views here.

