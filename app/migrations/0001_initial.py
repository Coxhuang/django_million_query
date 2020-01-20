# Generated by Django 3.0.2 on 2020-01-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('phone', models.CharField(max_length=64, verbose_name='手机号码')),
                ('email', models.CharField(max_length=64, verbose_name='邮箱地址')),
                ('add', models.CharField(max_length=128, verbose_name='地址')),
                ('cast', models.CharField(max_length=128, verbose_name='插入数据需要的时间')),
            ],
        ),
        migrations.CreateModel(
            name='MyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(max_length=128, verbose_name='节点')),
                ('time', models.CharField(max_length=128, verbose_name='时刻')),
            ],
        ),
    ]