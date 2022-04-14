"""socialproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registration_list),
    path('login', views.home_page),
    # creating and posting
    path('userlc/', views.UserListCreate.as_view()),
    path('postlc/', views.PostListCreate.as_view()),
    path('commentlc/', views.CommentListCreate.as_view()),
    path('grouplc/', views.GroupListCreate.as_view()),
    # performing CRUD operations on all models fields
    path('userlc/<int:pk>/', views.UserCrud.as_view()),
    path('postlc/<int:pk>/', views.PostCrud.as_view()),
    path('commentlc/<int:pk>/', views.CommentCrud.as_view()),
    path('grouplc/<int:pk>/', views.GroupCrud.as_view()),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
]
