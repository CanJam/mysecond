#！-*-coding:UTF-8-*-
import datetime #导入了 Python 的标准 datetime 模块
from django.db import models
from django.utils import timezone #和时区相关的 django.utils.timezone 工具模块

class Question(models.Model):  #Question 模型包括问题描述和发布时间
    question_text = models.CharField(max_length=200) #字符字段被表示为 CharField,要一个 max_length参数 
    pub_date = models.DateTimeField('date published') #日期时间字段被表示为 DateTimeField
    def __str__(self): #定义--str--（）很重要
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'
class Choice(models.Model):    #Choice 模型有两个字段，选项描述和当前得票数
    question = models.ForeignKey(Question,on_delete=models.CASCADE) #使用 ForeignKey定义了一个关系,每个 Choice 对象都关联到一个 Question 对象
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #votes 的 default 也就是默认值，设为0
    def __str__(self):
        return self.choice_text
class user(models.Model): #包含一个user和password
    user = models.CharField(max_length = 20)
    password = models.CharField(max_length = 100)
    # Create your models here.
#
"""
改变模型需要这三步：

    编辑 models.py 文件，改变模型。
    运行 python manage.py makemigrations 为模型的改变生成迁移文件。
    运行 python manage.py migrate 来应用数据库迁移
    """