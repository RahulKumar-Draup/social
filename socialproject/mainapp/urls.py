from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview),
    path('all/', views.getusers),
    path('posts/', views.getpost),
    path('group/', views.getgrp),
    path('check/', views.GroupApi.as_view()),
    path('comment/',views.CommentApi.as_view()),
    path('users/', views.UserApi.as_view()),
    path('post/', views.PostApi.as_view()),


]