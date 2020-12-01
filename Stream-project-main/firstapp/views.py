from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieData, SeriesData
from math import ceil
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
    obj = MovieData.objects.all() 
    return render(request,'Movies.html',{'obj':obj}) 

def TvseriesPage(request):
    obj = SeriesData.objects.all()
    return render(request,'Tvseries.html',{'obj':obj})

def Login(request):
    return render(request,'Login.html')

def SignUP(request):
    return render(request,'SignUP.html')