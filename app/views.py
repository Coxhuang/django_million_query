from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from faker import Faker
from app.models import MyModels
fake = Faker(locale='zh_CN') # 生成一个Faker对象(中文),默认不传参数时为英文
import datetime,time



class CreateDataApi(APIView):

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限

    def get(self,request):

        last = time.time()
        print(datetime.datetime.now()) # 2020-01-20 14:10:07.742492
        for foo in range(100000):
            MyModels.objects.create(
                name=fake.name(),
                phone=fake.phone_number(),
                email=fake.email(),
                add=fake.address(),
                cast=str(time.time()-last)
            )
            last = time.time()
        print(datetime.datetime.now()) # 2020-01-20 14:17:25.609981

        return Response({
            "success": False,
            "msg": "基类POST,请重新封装",
            "results": ""
        }, status=status.HTTP_200_OK)