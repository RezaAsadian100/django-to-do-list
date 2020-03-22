"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from todolist_app.views import ToDoList_Detail,ToDoList_Update,ToDoList_Delete,ToDoList_Add
from todolist_app import views as todo_views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('',todo_views.first,name='first'),
    path('home/',todo_views.home,name='user-home'),
    path('home/list/',todo_views.Usertodolist,name='list'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='todolist_app/first.html'),name='logout'),
    path('add/',ToDoList_Add.as_view(),name='add'),
    path('detail/<int:pk>/',ToDoList_Detail.as_view(),name='detail'),
    path('delete/<int:pk>/',ToDoList_Delete.as_view(),name='delete'),
    path('update/<int:pk>/',ToDoList_Update.as_view(),name='edit'),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile,name='profile'),
]
