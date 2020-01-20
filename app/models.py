from django.db import models

# Create your models here.



class MyModels(models.Model):

    # id = models.IntegerField(verbose_name="主键id",primary_key=True)
    name = models.CharField(verbose_name="姓名",max_length=64)
    phone = models.CharField(verbose_name="手机号码",max_length=64)
    email = models.CharField(verbose_name="邮箱地址",max_length=64)
    add = models.CharField(verbose_name="地址",max_length=128)
    cast = models.CharField(verbose_name="插入数据需要的时间",max_length=128)


class MyTime(models.Model):

    node = models.CharField(verbose_name="节点",max_length=128)
    time = models.CharField(verbose_name="时刻",max_length=128)