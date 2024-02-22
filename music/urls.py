from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),  
    path('login/', views.login_view, name='login'),
    path('profile/<int:artist_id>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search')
]