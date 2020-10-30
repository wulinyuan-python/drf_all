from rest_framework.response import Response
from rest_framework.views import APIView
from drf_day3.models import Book
from drf_day3.serializers import BookModelSerializer, BookDeModelSerializer, BookModelSerializerV2


# 写了get和post方法，这个得用到序列化器和反序列化器
class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book = Book.objects.get(pk=book_id)
            data = BookModelSerializer(book).data
            return Response({
                'status': 200,
                'message': '查看单个图书成功',
                'result': data,
            })
        else:  # 查询所有
            book_objects_all = Book.objects.all()
            book_ser = BookModelSerializer(book_objects_all, many=True).data

            return Response({
                'status': 200,
                'message': '查询所有图书成功',
                'result': book_ser,
            })


# 用了序列化总器，既能序列化，也能反序列化
class BookAPIViewV2(APIView):

    def get(self, request, *args, **kwargs):

        book_id = kwargs.get("id")

        if book_id:
            try:

                book = Book.objects.get(pk=book_id, is_delete=False)

                data = BookModelSerializerV2(book).data
            except Book.DoesNotExist:
                return Response({
                    'status': 400,
                    'message': '该图书不存在，请输入正确的id'
                })

            return Response({
                "status": 200,
                "message": "查询单个图书成功",
                "results": data,
            })

        else:
            book_objects_all = Book.objects.filter(is_delete=False)

            book_ser = BookModelSerializerV2(book_objects_all, many=True).data
            if not book_objects_all:
                return Response({
                    "status": 400,
                    "message": "库里好像没有书了哦",
                })
            return Response({
                "status": 200,
                "message": "查询所有图书成功",
                "results": book_ser,
            })

    def post(self, request, *args, **kwargs):
        """
        增加单个: 传递参数是字典
        增加多个: [{},{},{}] 列表中嵌套是一个个的图书对象
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        request_data = request.data

        if isinstance(request_data, dict):  # 代表添加的单个对象
            many = False
        elif isinstance(request_data, list):  # 代表添加的是多个对象
            many = True
        else:
            return Response({
                "status": 400,
                "message": "参数格式有误",
            })

        serializer = BookModelSerializerV2(data=request_data, many=many)

        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()

        return Response({
            "status": 200,
            "message": "添加图书成功",
            "results": BookModelSerializerV2(book_obj, many=many).data,
        })

    def delete(self, request, *args, **kwargs):
        """
        删除单个  删除多个
        单个删除: 通过json传递单个book_name
        多个删除: 有多个book_names {book_names:[1,2,3]}
        :return:
        """
        book_name = request.data.get('book_name')

        if book_name:
            # 删除单个
            book_names = [book_name]
        else:
            # 删除多个
            book_names = request.data.get("book_names")

        book_obj = Book.objects.filter(book_name__in=book_names, is_delete=False)
        print(book_obj)
        if not book_obj:
            return Response({
                "status": 400,
                "message": "该图书已删除"
            })
        response = book_obj.update(is_delete=True)
        if response:
            return Response({
                "status": 200,
                "message": '删除成功'
            })

        return Response({
            "status": 400,
            "message": '删除失败'
        })

    def put(self, request, *args, **kwargs):
        """
        整体修改单个:  修改一个对象的全部字段
        修改对象时,在调用序列化器验证数据时必须指定instance关键字
        在调用serializer.save() 底层是通过ModelSerializer内部的update()方法来完成的更新
        """

        # 获取要修改的对象的值
        request_data = request.data
        # print(request_data)
        # 获取要修改的图书的名字
        # 查询单个
        book_name = kwargs.get("id")
        if book_name:
            try:
                book_obj = Book.objects.get(book_name=book_name)
            except Book.DoesNotExist:
                return Response({
                    "status": 400,
                    "message": '图书不存在'
                })
            serializer = BookModelSerializerV2(data=request_data, instance=book_obj, partial=True)
            serializer.is_valid(raise_exception=True)

            # 经过序列化器对   全局钩子与局部钩子校验后  开始更新
            serializer.save()

            return Response({
                "status": 200,
                "message": '修改成功',
                "results": BookModelSerializerV2(book_obj).data
            })

        # 查询多个
        else:
            book_objs = []
            for i in range(len(request_data)):
                book_name = request_data[i].get('id')
                # print(book_name)
                try:
                    book_obj = Book.objects.get(book_name=book_name)
                    print(book_obj)
                except Book.DoesNotExist:
                    return Response({
                        "status": 400,
                        "message": '图书不存在'
                    })
                serializer = BookModelSerializerV2(data=request_data[i], instance=book_obj)
                serializer.is_valid(raise_exception=True)

                # 经过序列化器对   全局钩子与局部钩子校验后  开始更新
                serializer.save()
                book_objs.append(book_obj)
            return Response({
                "status": 200,
                "message": '修改成功',
                "result" : BookModelSerializerV2(book_objs, many=True).data,
            })

    def patch(self, request, *args, **kwargs):
        """
        整体修改单个:  修改一个对象的部分字段
        修改对象时,在调用序列化器验证数据时必须指定instance关键字
        在调用serializer.save() 底层是通过ModelSerializer内部的update()方法来完成的更新
        """

        # 获取要修改的对象的值
        request_data = request.data
        # print(request_data)
        # 获取要修改的图书的名字
        # 查询单个
        book_name = kwargs.get("id")
        if book_name:
            try:
                book_obj = Book.objects.get(book_name=book_name)
            except Book.DoesNotExist:
                return Response({
                    "status": 400,
                    "message": '图书不存在'
                })
            serializer = BookModelSerializerV2(data=request_data, instance=book_obj, partial=True)
            serializer.is_valid(raise_exception=True)

            # 经过序列化器对   全局钩子与局部钩子校验后  开始更新
            serializer.save()

            return Response({
                "status": 200,
                "message": '修改成功',
                "results": BookModelSerializerV2(book_obj).data
            })

        # 查询多个
        else:
            book_objs = []
            for i in range(len(request_data)):
                book_name = request_data[i].get('id')
                # print(book_name)
                try:
                    book_obj = Book.objects.get(book_name=book_name)
                    print(book_obj)
                except Book.DoesNotExist:
                    return Response({
                        "status": 400,
                        "message": '图书不存在'
                    })
                serializer = BookModelSerializerV2(data=request_data[i], instance=book_obj, partial=True)
                serializer.is_valid(raise_exception=True)

                # 经过序列化器对   全局钩子与局部钩子校验后  开始更新
                serializer.save()
                book_objs.append(book_obj)
            return Response({
                "status": 200,
                "message": '修改成功',
                "result":BookModelSerializerV2(book_objs, many=True).data,
            })

        # 更新的时候需要对前端传递的数据进行安全校验
        # 更新的时候需要指定关键字参数data
        # TODO 如果是修改  需要自定关键字参数instance  指定你要修改的实例对象是哪一个

