#！-*-coding：UTF-8-*-
from django.urls import path
from .import views
#函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name
urlpatterns = [
       path('',views.index,name='index'),#path(‘’（链接），方法名，name=‘’)，path的格式
       # path('nono/',views.nono,name='i'),#自己测试语句，

]