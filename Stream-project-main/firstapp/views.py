from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieData, SeriesData
# Create your views here.

def MovComingSoon(request):
    return render(request,'MovComingSoon.html')

def MovInTheater(request):
    return render(request,'MovInTheater.html')

def MovMostView(request):
    return render(request,'MovMostView.html')

def MovTopRated(request):
    return render(request,'MovTopRated.html') 

def HomePage(request):
    obj = SeriesData.objects.all()
    obj2 = MovieData.objects.all() 
    return render(request,'Homepage.html',{'obj':obj , 'obj2':obj2}) 

def MoviePage(request):
    return render(request,'Movies.html') 

def TvseriesPage(request):
    return render(request,'Tvseries.html')

def Login(request):
    return render(request,'Login.html')

def SignUP(request):
    return render(request,'SignUP.html')