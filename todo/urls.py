from django.urls import path
from .views import *


urlpatterns=[

    #------Home Page------

    path("",home,name=""),
   

    #-----------REGISTER a USER-----
    
    path("register",register,name='register'),


    #-------Login User--------

    path("my-login",my_login,name='my-login'),



   #------Dashboard Page------ 

    path("dashboard",dashboard,name='dashboard'),


    #-------Profile Management-----

    path("profile-management",profile_management,name='profile-management'),



    #-------Profile Management-----

    path("delete-account",deleteAccount,name='delete-account'),
   


    #-------CREATE a Task-----

    path("create-task",createTask,name='create-task'),


    #-------Read or View a Task-----

    path("view-tasks",viewTask,name='view-tasks'),


    #-------Update a Task-----

    path("update-task/<str:pk>/",updateTask,name='update-task'),



    #-------Delete a Task-----

    path("delete-task/<str:pk>/",deleteTask,name='delete-task'),




    #-------Logout User======

    path("user-logout",user_logout,name='user-logout'),

]





    # #  CRUD operations

    # path("create-task",createTask,name="create-task"),
    # path("view-tasks",viewTasks,name="view-tasks"),
    # path("update-task/<str:pk>/",updateTask,name="update-task"),
    # path("delete-task/<str:pk>/",deleteTask,name="delete-task"),


