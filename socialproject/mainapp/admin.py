from django.contrib import admin
from .models import Group, Post, Comment,User

# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'group_type', 'modified_on', 'created_on']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_msg', 'created_by', 'approved', 'modified_on', 'created_on']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'comment_msg', 'created_on']


