from django.urls import path

from UserApp import views


urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('Register', views.Register),
    path('RegAction', views.RegAction),
    path('LogAction', views.LogAction),
    path('CustomerHome', views.CustomerHome),
    path('GroupChat', views.GroupChat),
    path('GroupChatAction', views.GroupChatAction),
    path('GroupReply', views.GroupReply),
    path('ReplyNow.html', views.ReplyNow),
    path('ReplyChatAction', views.ReplyChatAction),
    path('ViewService', views.ViewService),
    path('ChatWroker', views.ChatWroker),
    path('ChatAction', views.ChatAction),
    path('ViewReplay', views.ViewReplay),
    path('BookService', views.BookService),
    path('viewbookings', views.viewbookings),
]
