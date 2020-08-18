# from django.contrib import admin
import xadmin
from .models import *
from xadmin.views.website import LoginView
from xadmin.views import CommAdminView
# Register your models here.

#对学生信息类进行注册和页面自定义展示操作
class StudentsAdmin(object):
    list_display = ('name', 'sex', 'age', 'address',)
    style_fields = {'subjects': 'checkbox-inline', }
    # search_fields = ('name',)
    #性别过滤
    list_filter = ('sex',)
    #通过名字 课程 班级查询
    search_fields = ('name', 'class_name__class_name', 'subjects__name',)

    # 顺序排序
    ordering = ('age', 'name',)
    # 逆序排序，在前面加一个减号"-"，例如按年龄倒序排列
    ordering = ('-age',)


xadmin.site.register(Students, StudentsAdmin)

#对班级类进行注册和页面自定义展示操作
class ClassAdmin(object):
    list_display = ('class_name',)

xadmin.site.register(Class, ClassAdmin)

#对课程学分类进行注册和页面自顶也展示操作
class SubjectsAdmin(object):
    list_display = ('name', 'score',)

xadmin.site.register(Subjects, SubjectsAdmin)

#对教师信息进行注册和页面自定义展示操作
class TeachersAdmin(object):
    list_display = ('name',)

xadmin.site.register(Teachers, TeachersAdmin)

#显示站点的名称
class LoginViewAdmin(LoginView):
    title = '学生信息管理系统'

xadmin.site.register(LoginView, LoginViewAdmin)

#修改其他信息 版权地址
class GlobalSetting(CommAdminView):
    # 左上角及浏览器标题
    site_title = '学生信息管理系统'
    # 页脚版权信息
    site_footer = 'Copyright © 2020 overburdeni'
    #优化页面
    menu_style = 'accordion'

xadmin.site.register(CommAdminView, GlobalSetting)

