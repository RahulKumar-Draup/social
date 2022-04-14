
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User, Group, Post, Comment
# from rest_framework import serializers
from. serializers import UserSerializer, GroupSerializer, PostSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,\
    DjangoModelPermissions, IsAdminUser



@api_view(['GET'])

def registration_list(request):
    x = {
        'Create new account': 'http://127.0.0.1:8000/userlc/',
        'LOGIN': 'http://127.0.0.1:8000/login',

    }
    return Response(x)


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
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
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


class CommentListCreate(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


class GroupListCreate(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserCrud(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


class PostCrud(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


class CommentCrud(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


class GroupCrud(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]



