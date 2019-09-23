from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gogetthegood/', views.goGetTheGood, name ='go_get_the_good'),
    path('happyhappyjoyjoy/', views.happyHappyJoyJoy, name ='happy_happy_joy_joy'),
    path('endpoint/', views.endPoint, name ='end_point'),
    path('endpoint/<str:userinput>/', views.index, name ='end_point'),
]
