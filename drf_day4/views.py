from django.shortcuts import render
from rest_framework import viewsets
from drf_day4.models import Workers

# Create your views here.
from rest_framework.response import Response

class WorkersViewSetView(viewsets.ViewSet):
    def login(self,request,*args,**kwargs):
        print(request.data)
        w_name = request.data['w_name']
        password = request.data['password']
        objects_filter = Workers.objects.filter(w_name=w_name, password=password)
        if objects_filter:
            return Response({
                'status': 200,
                'message': '登录成功',
                'result': objects_filter.values(),
            })
        else:
            return Response({
                'status':400,
                'message':'登录失败，请检查用户名和密码是否正确'
            })

    def register(self,request,*args,**kwargs):
        print(request.data)
        w_name = request.data['w_name']
        password = request.data['password']
        objects_filter = Workers.objects.filter(w_name=w_name, password=password)
        if not objects_filter:
            try:
                worker = Workers.objects.create(w_name=w_name,password=password)
                worker.save()
                return Response({
                    'status':200,
                    'message':'注册成功',
                    'result':worker.w_name
                })
            except:
                return Response({
                    'status':400,
                    'message':'注册失败,请检查参数是否正确'
                })
        else:
            return Response({
                'status':400,
                'message':'该用户名已存在'
            })