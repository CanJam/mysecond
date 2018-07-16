#！-*-coding：UTF-8-*-
from django.urls import path
from .import views
#函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name
app_name = 'polls' #为 URL 名称添加命名空间
"""
urlpatterns = [
       path('',views.index,name='index'),#path(‘’（链接），方法名，name=‘’)，path的格式
       # path('nono/',views.nono,name='i'),#自己测试语句，
       path('<int:question_id>/', views.detail, name='detail'),
       path('<int:question_id>/results/',views.results,name='results'),#结果页
       path('<int:question_id>/vote/',views.vote,name='vote'), #投票页
]
"""
#优化1：导入通用试图
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]