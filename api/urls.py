from django.urls import path

from . import views


urlpatterns = [
	path('chats/', views.ChatListView.as_view()),
]