import datetime
from . permission import Writebyadmin
# Writebymoderator
from datetime import date, timedelta
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User, Group, Post, Comment
from. serializers import UserSerializer, GroupSerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated




@api_view(['GET'])
@authentication_classes([SessionAuthentication])
def registration_list(request):
    x = {
        'user': 'http://127.0.0.1:8000/user/',
        'posts': 'http://127.0.0.1:8000/posts/',
        'group': 'http://127.0.0.1:8000/group/',
        'delete inactive user': 'http://127.0.0.1:8000/delete/',
        'comment': 'http://127.0.0.1:8000/comment/',


        'message': 'to delete or update use pk of obj',
    }
    return Response(x)


"""mail sending list and function"""


@api_view(['GET'])
def mail(request):
    # val = request.user if type(request.user) is not AnonymousUser else None
    try:
        lst = []
        res = User.objects.all()
        for i in range(len(res)):
            lst.append(res[i].email)
        send_mail(
            'test mail',
            'This is a test mail',
            'rahul992134@gmail.com',
            lst,
            fail_silently=False
        )
        print(lst)
        return Response(lst)
    except User.DoesNotExist:
        pass


"""API VIEW OF USERS"""


@api_view(['get', 'POST'])
def listandretrive(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        userserializer = UserSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return Response(userserializer.data, status=status.HTTP_201_CREATED)
        return Response(userserializer.errors)


@api_view(['PUT', 'GET', 'DELETE'])
# permission to admin ,user,and moderator
@permission_classes([IsAuthenticated])
def usermanag(request, pk):
    try:
        lst = []
        user = User.objects.get(id=pk)
        lst.append(user.email)
        send_mail(
            'activity in group',
            'check activity in group',
            'rahul992134@gmail.com',
            lst,
            fail_silently=False
        )
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        userserializer = UserSerializer(user)
        return Response(userserializer.data)
    elif request.method == 'PUT':
        userserializer = UserSerializer(user, data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return Response(userserializer.data)
        return Response(userserializer.errors)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""API VIEW OF POSTS"""


@api_view(['get', 'POST'])
def listandviewpost(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        userserializer = PostSerializer(data=request.data)
        if userserializer.is_valid():
            userserializer.save()
            return Response(userserializer.data, status=status.HTTP_201_CREATED)
        return Response(userserializer.errors)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def postmanag(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        postserializer = PostSerializer(post)
        return Response(postserializer.data)
    elif request.method == 'PUT':
        postserializer = PostSerializer(post, data=request.data)
        if postserializer.is_valid():
            postserializer.save()
            return Response(postserializer.data)
        return Response(postserializer.errors)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""API VIEW OF COMMENTS"""


@api_view(['get', 'POST'])
def listandviewcomment(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        commentserializer = CommentSerializer(data=request.data)
        if commentserializer.is_valid():
            commentserializer.save()
            return Response(commentserializer.data, status=status.HTTP_201_CREATED)
        return Response(commentserializer.errors)


@api_view(['PUT', 'GET', 'DELETE'])
def commentmanag(request, pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        commentserializer = CommentSerializer(comment)
        return Response(commentserializer.data)
    elif request.method == 'PUT':
        commentserializer = CommentSerializer(comment, data=request.data)
        if commentserializer.is_valid():
            commentserializer.save()
            return Response(commentserializer.data)
        return Response(commentserializer.errors)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""API VIEW OF GROUPS"""


@api_view(['GET', 'POST'])
def listandviewgroup(request):
    if request.method == "GET":
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        groupserializer = GroupSerializer(data=request.data)
        if groupserializer.is_valid():
            groupserializer.save()
            return Response(groupserializer.data, status=status.HTTP_201_CREATED)
        return Response(groupserializer.errors)


@api_view(['PUT', 'GET', 'DELETE'])
# permission to only admin
@permission_classes([Writebyadmin])
def groupmanag(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        groupserializer = GroupSerializer(group)
        return Response(groupserializer.data)
    elif request.method == 'PUT':
        groupserializer = CommentSerializer(group, data=request.data)
        if groupserializer.is_valid():
            groupserializer.save()
            return Response(groupserializer.data)
        return Response(groupserializer.errors)
    elif request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  to delete inactive user only by admin
@api_view(['GET', 'DELETE'])
@permission_classes([Writebyadmin])
def deleteinactive(request):
    lst = []
    current_day = date.today()
    previous_day = current_day-timedelta(1)
    users = User.objects.all()

    for i in range(len(users)):
        if not users[i].is_active:
            lst.append(users[i].username)
    print(lst)
    send_mail(
        'account deletion',
        'your profile is deleted for being inactive',
        'rahul992134@gmail.com',
        lst,
        fail_silently=False
    )
    for elem in lst:
        users.delete()
    return Response(lst)
