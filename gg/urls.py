from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('profile/deleteProfile', views.deleteProfile),
    path('makeProfile/deleteProfile', views.deleteProfile),
    path('games/', views.games),
    path('games/classic/', views.games_classic),
    path('games/fps/', views.games_fps),
    path('games/rpg/', views.games_rpg),
    path('games/adventure/', views.games_adventure),
    path('makeProfile/', views.makeProfile, name='makeProfile'),
    path('makeProfile/addProfile', views.addProfile, name='addProfile'),
    path('makeReview/', views.makeReview, name='makeReview'),
    path('makeReview/addReview', views.addReview, name='addReview'),
    path('chat/', views.chat, name='chat'),
    path('', views.homepage, name='homepage'),
    path('chat/chat/<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name = 'send'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
