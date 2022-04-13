from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Group(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    group_type = models.CharField(max_length=100, choices=(
        ('PUBLIC', 'public'),
        ('PRIVATE', 'private'),
    ))

    is_admin = models.ManyToManyField(User, related_name='Admin', blank=True)
    is_moderator = models.ManyToManyField(User, related_name="Moderator", blank=True)
    is_member = models.ManyToManyField(User, related_name="Member", blank=True)
    modified_on = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name


class Post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    post_msg = models.TextField(max_length=1000, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    approved = models.BooleanField()
    modified_on = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commented_by = models.ManyToManyField(User, default='')
    comment_msg = models.CharField(max_length=100, default='')
    created_on = models.DateTimeField(auto_now_add=True)
