from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from faker import Faker
from app import models
fake = Faker(locale='zh_CN') # 生成一个Faker对象(中文),默认不传参数时为英文
import datetime,time,random
from django.db import transaction



class CreateDataApi(APIView):

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限

    def get(self,request):

        # with transaction.atomic():  # 事务回滚

            # for foo in range(1, 1000001): # 学生 百万
            #     user = models.UserProfile.objects.create(
            #         name=fake.name(),
            #         age=fake.date(),
            #         address=fake.address(),
            #     )
            #     models.Students.objects.create(
            #         user=user,
            #         stu_id=fake.credit_card_number()
            #     )

            # for foo in range(100000): # 教师 十万
            #     user = models.UserProfile.objects.create(
            #         name=fake.name(),
            #         age=fake.date(),
            #         address=fake.address(),
            #     )
            #     tea_obj = models.Teachers.objects.create(
            #         user=user,
            #     )
            #     for j in range(1,11):
            #         stu_obj = models.Students.objects.get(user_id=j+foo*10)
            #         tea_obj.stu.add(stu_obj)
            #         tea_obj.save()

        for foo in range(1, 300001):
            tea_id = (foo + 2) // 3
            tea_obj = models.Teachers.objects.get(id=tea_id)
            course_obj = models.Course.objects.create(
                course_name=fake.company(),
                tea=tea_obj
            )
            for j in range(1, 4):
                # print(foo, 3 * (foo - 1) + j)
                stu_id = 3 * (foo - 1) + j
                stu_obj = models.Students.objects.get(id=stu_id)
                course_obj.stu.add(stu_obj)
                course_obj.save()

        for foo in range(900000,1000001):
            stu_obj = models.Students.objects.get(id=foo)

            for j in range(1,5):
                course_id = random.randint(1,300000)
                course_obj = models.Course.objects.get(id=course_id)
                course_obj.stu.add(stu_obj)
                course_obj.save()

        return Response({
            "success": False,
            "msg": "基类POST,请重新封装",
            "results": ""
        }, status=status.HTTP_200_OK)

class GetDataApi(APIView):

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限

    def get(self,request):

        print(datetime.datetime.now()) #
        # obj_list = MyModels.objects.filter(id__lte=100000)
        # print(len(obj_list))
        # for foo in obj_list:
        #     # print(foo)
        #     a = foo
        print(datetime.datetime.now()) #

        return Response({
            "success": False,
            "msg": "查数据",
            "results": ""
        }, status=status.HTTP_200_OK)