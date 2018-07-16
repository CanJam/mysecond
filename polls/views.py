#！-*-coding：UTF-8-*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Question,Choice
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
 # return HttpResponse('nonoo')  
"""
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
"""
#优化2：引用get_object_or_404()
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})    
"""
def results(request, question_id):    
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
#优化1：当有人对 Question 进行投票后， vote() 视图将请求重定向到 Question 的结果界面
"""
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})    
"""
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    
优化1：引入404异常,
request.POST 是一个类字典对象，通过关键字的名字获取提交的数据。 
request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID,值永远是字符串。
如果在 request.POST['choice'] 数据中没有提供 choice ， POST 将引发一个 KeyError 。
代码检查 KeyError ，如果没有给出 choice 将重新显示 Question 表单和一个错误信息
在 HttpResponseRedirect 的构造函数中使用 reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL。
它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数
"""
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
            })    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))        
# Create your views here.

