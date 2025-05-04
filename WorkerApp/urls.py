from django.urls import path

from WorkerApp import views
urlpatterns = [
    path('login', views.login),
    path('SPRegister', views.SPRegister),
    path('RegAction', views.RegAction),
    path('LoginAction', views.LoginAction),
    path('SPHome', views.SPHome),
    path('viewMessage', views.viewMessage),
    path('ReplyUser', views.ReplyUser),
    path('ChatAction', views.ChatAction),
    path('viewBooking', views.viewBooking),
    path('GroupChat', views.GroupChat),
    path('AcceptService', views.AcceptService)


]
