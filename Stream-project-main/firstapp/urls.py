from django.urls import path
from . import views 

urlpatterns = [
path('', views.HomePage,name="Home") ,
path('movies/', views.MoviePage, name="Movies" ) ,
path('tvseries/',views.TvseriesPage,name="TV") ,
path('login/',views.Login,name='Login'),
path('register/',views.SignUP,name='Sup'),

path('movcomingsoon/',views.MovComingSoon,name='MCS'), 
path('movintheater/',views.MovInTheater,name='MIT'),
path('movmostviewed/',views.MovMostView,name='MMV'),
path('movtoprated/',views.MovTopRated,name='MTR'),

]