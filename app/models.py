from django.db import models
import os

# Create your models here.
#添加班级类
class Class(models.Model):
    class_name = models.CharField(verbose_name='班级', max_length=100)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __str__(self):
        return self.class_name

#添加课程学分数据类
class Subjects(models.Model):
    name = models.CharField(verbose_name='课程名称', max_length=50, blank=True)
    score = models.IntegerField(verbose_name='学分', blank=True)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'

    def __str__(self):
        return self.name

#添加教师类
class Teachers(models.Model):
    name = models.CharField(verbose_name='教师名称',max_length=50,blank=True)

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'

    def __str__(self):
        return self.name
#添加学生信息类
class Students(models.Model):
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    # sex = models.CharField(verbose_name='性别', max_length=50)
    sex = models.CharField(choices=SEX, verbose_name='性别', max_length=50)
    age = models.IntegerField(verbose_name='年龄')
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='入学时间')
    remarks = models.TextField(verbose_name='备注', blank=True)
    subjects = models.ManyToManyField(Subjects, verbose_name='选修课程',blank=True)

    headmaster = models.OneToOneField(Teachers, verbose_name='班主任', on_delete=models.CASCADE, blank=True, null=True)
    # grade_name = models.ForeignKey(Grade, verbose_name='所在年级', on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ForeignKey(Class, verbose_name='所在班级', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return self.name

    #路径获取方法
    def get_photo(self, filename):
        return os.path.join('photo',
                            '%s_%s_%s_%s' % (self.class_name, self.name, self.id, os.path.splitext(filename)[1]))

    photo = models.ImageField(verbose_name='照片', upload_to=get_photo, blank=True, null=True)





