from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name='logout'),
    path('feed/', views.feed, name='feed'),
    path('add_to_shelf/', views.addToShelf, name="add_to_shelf"),
    path('book/<str:pk>/', views.book, name='book'),
    path('trending/', views.trending, name='trending'),
    path('community/', views.groups, name="community"),
    path('group/<str:pk>', views.group, name="group"),
    path('my-books/', views.myBooks, name="my-books"),
    path('add_review/', views.addReview, name="add_review"),
    path('add_message/', views.addMessage, name="add_message"),
    path('delete_message/<str:pk>', views.deleteMessage, name="delete_message"),
    path('profile/<str:pk>', views.userProfile, name="profile"),
    path('newsarticles/', views.newsarticles, name="newsarticles"),
    path('newsarticle/<str:pk>', views.newsarticle, name="newsarticle"),
    path('news-article-form/', views.newsArticleForm, name="news-article-form"),
    path('create-article/', views.createArticle, name="create-article"),
    path('create-group/', views.createGroup, name="create-group"),
    path('send-friend-request/<str:pk>', views.sendFriendRequest, name="send-friend-request"),
    path('accept-friend-request/', views.acceptFriendRequest, name="accept-friend-request"),
    path('notifications/', views.notifications, name="notifications"),
    path('search-result/', views.search, name="search-result"),
    path('filter-genre/<str:pk>', views.filterGenre, name="filter-genre"),
    
]
