from django.urls import path
from . import views 

urlpatterns = [
path('', views.HomePage,name="Home") ,
path('movies/', views.MoviePage, name="Movies" ) ,
path('tvseries/',views.TvseriesPage,name="TV") ,
path('login/',views.Login,name='Login'),
path('register/',views.SignUP,name='Sup'),
]