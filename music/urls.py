from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),  # Add 'views.' prefix here
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]