from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_day6.authentication import JWTAuthentication
from drf_day6.filter import ComputerFilterSet
from drf_day6.models import Computer
from drf_day6.serializer import UserModelSerializer, ComputerModelSerializer


class UserDetailAPIView(APIView):
    """
    只能登陆以后才能访问
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        return Response("OK")


class LoginAPIView(APIView):
    """
    实现多方式登陆：手机号  邮箱  用户  三者任意一个与密码匹配即可登陆成功
    # 1. 禁用权限与认证组件
    # 2. 获取前端传递的参数
    # 3. 校验前端传递的参数来得到对应的用户
    # 4. 签发token并返回
    """
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        # 前端账号来传递用户标识 account  密码使用password
        # account = request.data.get("account")
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = {
            "token": serializer.token,
            "user": UserModelSerializer(serializer.obj).data
        }
        print(data)

        return Response(data)


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # 通过filter_backends来配置你要使用的过滤器类
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    # 指定你要搜索的字段|条件
    search_fields = ['name', "price"]
    # 指定排序的条件
    ordering = ['price']

    # 分页器的使用
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination

    # 查询价格大于 3000  小于8000的电脑
    # django-filter查询  通过filter_class 指定过滤器
    filter_class = ComputerFilterSet
