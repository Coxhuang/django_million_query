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

        # for foo in range(1, 300001):
        #     tea_id = (foo + 2) // 3
        #     tea_obj = models.Teachers.objects.get(id=tea_id)
        #     course_obj = models.Course.objects.create(
        #         course_name=fake.company(),
        #         tea=tea_obj
        #     )
        #     for j in range(1, 4):
        #         # print(foo, 3 * (foo - 1) + j)
        #         stu_id = 3 * (foo - 1) + j
        #         stu_obj = models.Students.objects.get(id=stu_id)
        #         course_obj.stu.add(stu_obj)
        #         course_obj.save()
        #
        # for foo in range(900000,1000001):
        #     stu_obj = models.Students.objects.get(id=foo)
        #
        #     for j in range(1,5):
        #         course_id = random.randint(1,300000)
        #         course_obj = models.Course.objects.get(id=course_id)
        #         course_obj.stu.add(stu_obj)
        #         course_obj.save()

        return Response({
            "success": False,
            "msg": "基类POST,请重新封装",
            "results": ""
        }, status=status.HTTP_200_OK)

class GetORMUserDataApi(APIView):

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限

    def get(self,request):
        """
        小数据查询,验证sql语句
        :param request:
        :return:
        """
        print("没有使用优化ORM-起始时间:{}".format(datetime.datetime.now()))  #
        obj_list = models.UserProfile.objects.filter(id__lte=5)
        print("数据量:{}".format(len(obj_list)))  #
        for foo in obj_list:
            temp = foo.name
        print("没有使用优化ORM-结束时间:{}".format(datetime.datetime.now()))  #
        print("\n")
        print("------------------------")
        print("\n")
        print("优化ORM-起始时间:{}".format(datetime.datetime.now()))  #
        obj_list = models.UserProfile.objects.select_related().filter(id__lte=5)
        print("数据量:{}".format(len(obj_list)))  #
        for foo in obj_list:
            temp = foo.name
        print("优化ORM-结束时间:{}".format(datetime.datetime.now()))  #

        return Response({
            "success": False,
            "msg": "小数据查询",
            "results": ""
        }, status=status.HTTP_200_OK)

    def post(self,request):
        """
        大数据查询-验证耗时
        :param request:
        :return:
        """
        print("没有使用优化ORM-起始时间:{}".format(datetime.datetime.now()))  #
        obj_list = models.UserProfile.objects.all()
        print("数据量:{}".format(len(obj_list)))  #
        for foo in obj_list:
            temp = foo.name
        print("没有使用优化ORM-结束时间:{}".format(datetime.datetime.now()))  #
        print("\n")
        print("------------------------")
        print("\n")
        print("优化ORM-起始时间:{}".format(datetime.datetime.now()))  #
        obj_list = models.UserProfile.objects.select_related().all()
        print("数据量:{}".format(len(obj_list)))  #
        for foo in obj_list:
            temp = foo.name
        print("优化ORM-结束时间:{}".format(datetime.datetime.now()))  #

        return Response({
            "success": False,
            "msg": "大数据查询",
            "results": ""
        }, status=status.HTTP_200_OK)


class GetORMTeachersDataApi(APIView):

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限

    def get(self,request):

        print("没有使用优化ORM-起始时间:{}".format(datetime.datetime.now())) #
        obj_list = models.Teachers.objects.filter(id__lte=10)
        print("数据量:{}".format(len(obj_list))) #
        for foo in obj_list:
            print(foo.user)
        print("没有使用优化ORM-结束时间:{}".format(datetime.datetime.now())) #
        print("\n")
        print("------------------------")
        print("\n")
        print("优化ORM-起始时间:{}".format(datetime.datetime.now()))  #
        obj_list = models.Teachers.objects.select_related().filter(id__lte=10)
        print("数据量:{}".format(len(obj_list)))  #
        for foo in obj_list:
            print(foo.user)
        print("优化ORM-结束时间:{}".format(datetime.datetime.now()))  #

        return Response({
            "success": False,
            "msg": "ORM无优化-查数据-教师表-十万数据",
            "results": ""
        }, status=status.HTTP_200_OK)