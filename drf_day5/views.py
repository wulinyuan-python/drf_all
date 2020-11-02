from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from drf_day5.authentications import MyAuth
from drf_day5.models import User5
from drf_day5.permission import MyPermission
from drf_day5.throttle import SendMessageRate


class Demo(APIView):

    def get(self, request, *args, **kwargs):
        user = User5.objects.first()
        print(user)
        print(user.groups.first())
        print(user.user_permissions.first())

        return Response("OK")


class UserAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [MyPermission]

    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        print("读请求")
        return Response("读请求")

    def post(self, request, *args, **kwargs):
        print("写请求")
        return Response("写请求")
