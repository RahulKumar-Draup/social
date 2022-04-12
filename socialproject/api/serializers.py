from rest_framework import serializers
from socialproject.mainapp.models import User, Group, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        models = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        models = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = '__all__'

