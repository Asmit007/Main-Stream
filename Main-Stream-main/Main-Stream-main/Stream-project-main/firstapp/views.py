from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieData, SeriesData
# Create your views here.

def HomePage(request):
    return render(request,'Homepage.html') 

def MoviePage(request):
    obj = MovieData.objects.all()
    print(obj)
    return render(request,'Movies.html', {'obj':obj}) 

def TvseriesPage(request):
    return render(request,'Tvseries.html')

def Login(request):
    return render(request,'Login.html')

def SignUP(request):
    return render(request,'SignUP.html')