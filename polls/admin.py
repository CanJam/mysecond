#！-*-coding：UTF-8-*-
from django.contrib import admin
from .models import Question,Choice


"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
#需要遵循以下流程——创建一个模型后台类，接着将其作为第二个参数传给 admin.site.register() ——在你需要修改模型的后台管理选项时这么做
class QuestionAdmin(admin.ModelAdmin):
    #fieldsets 元组中的第一个元素是字段集的标题
      fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
        inlines = [ChoiceInline]
        """
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]    
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']  #允许人们以 pub_date 字段来过滤列表  
    search_fields = ['question_text'] #在列表的顶部增加一个搜索框
admin.site.register(Question,QuestionAdmin)

# Register your models here.
