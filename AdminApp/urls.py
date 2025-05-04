from django.urls import path

from AdminApp import views
urlpatterns = [
    path('login', views.login),
    path('AdminAction', views.AdminAction),
    path('addservice', views.addservice),
    path('adminhome', views.AdminHome),
    path('serviceaction', views.serviceaction),
    path('viewserivces', views.viewserivces),

]
