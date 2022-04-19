from django.core.mail import send_mail
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from .models import User, Group, Post, Comment
from. serializers import UserSerializer, GroupSerializer, PostSerializer, CommentSerializer


@api_view(['GET'])
def registration_list(request):

    x = {
        'Create new account': 'http://127.0.0.1:8000/userlc/',
        'LOGIN': 'http://127.0.0.1:8000/login',
    }
    return Response(x)


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
def home_page(request):
    y = {
        'post list and create ': 'http://127.0.0.1:8000/postlc/',
        'comment list and crate': 'http://127.0.0.1:8000/commentlc/',
        'group list and create': 'http://127.0.0.1:8000/grouplc/',
    }
    return Response(y)


class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GroupListCreate(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserCrud(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostCrud(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentCrud(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GroupCrud(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]


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

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def private(request):
#     lst = []
#     val = request.user if type(request.user) is not AnonymousUser else None
#     res = Group.objects.all()
#     for i in range(len(res)):
#         print(res[i].group_type)
#         if res[i].group_type == 'PRIVATE':
#             lst.append(res[i].group_name)
#     return Response(lst)


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
def usermanag(request, pk):
    try:
        user = User.objects.get(id=pk)
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


@api_view(['get', 'POST'])
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


class writebyadmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        user = request.user
        if request.method == 'GET':
            return True
        elif request.method == 'POST' or request.method == 'Put' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False
