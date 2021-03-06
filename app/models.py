from django.db import models

"""
用户信息 -> 一对一 -> 学生表
用户信息 -> 一对一 -> 教师表

学生表 -> 多对多 -> 教师表(m)

教师表 -> 一对多 -> 课程表(fk)

学生表 -> 多对多 -> 课程表(m)
"""

class UserProfile(models.Model):
    """用户信息"""
    name = models.CharField(verbose_name="姓名",max_length=128)
    age = models.CharField(verbose_name="年龄",max_length=128)
    address = models.CharField(verbose_name="地址",max_length=128)

class Students(models.Model):
    """学生表"""
    user = models.OneToOneField(to=UserProfile,on_delete=models.DO_NOTHING)
    stu_id = models.CharField(verbose_name="学号",max_length=128)

class Teachers(models.Model):
    """老师表"""
    user = models.OneToOneField(to=UserProfile,on_delete=models.DO_NOTHING)
    stu = models.ManyToManyField(to=Students)

class Course(models.Model):
    """课程表"""
    course_name = models.CharField(verbose_name="课程名",max_length=128)
    stu = models.ManyToManyField(to=Students)
    tea = models.ForeignKey(to=Teachers,on_delete=models.DO_NOTHING)

