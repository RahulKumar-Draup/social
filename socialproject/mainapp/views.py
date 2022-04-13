
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Group, Post, Comment
# from rest_framework import serializers
from. serializers import UserSerializer, GroupSerializer, PostSerializer, CommentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import generics


@api_view(['GET'])
def overview(request):
    api_urls = {
        'Create NEW user': 'http://127.0.0.1:8000/create/users/',
        'ADD NEW GROUP': 'http://127.0.0.1:8000/api/check/',
        'MAKE POST': 'http://127.0.0.1:8000/make/post/',
        'VIEW ALL USER JSON ': 'http://127.0.0.1:8000/getuser/all/',
        'VIEW ALL GROUP JSON': 'http://127.0.0.1:8000/all/group/',
        'VIEW ALL POSTS JSON': 'http://127.0.0.1:8000/postbyuser/posts/'

    }
    return Response(api_urls)


@api_view(['GET'])
def getusers(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    # for detail in serializer.data:
    #     print(detail)
    return Response(serializer.data)


@api_view(['GET'])
def getgrp(request):
    user = Group.objects.all()
    serializer = GroupSerializer(user, many=True)
    # for detail in serializer.data:
    #     print(detail)
    return Response(serializer.data)


@api_view(['GET'])
def getpost(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


class GroupApi(CreateModelMixin, GenericAPIView):
    quaryset = Group.objects.all()
    serializer_class = GroupSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except Exception :
            return Response({
                "message": "Failed"
            })


class UserApi(CreateModelMixin, GenericAPIView):
    quaryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except Exception :
            return Response({
                "message": "Failed"
            })


class PostApi(CreateModelMixin, GenericAPIView):
    quaryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except Exception:
            return Response({
                "message": "Failed"
            })
