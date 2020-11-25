from django.contrib import admin

# Register your models here.
from .models import MovieData, SeriesData

admin.site.register(MovieData)
admin.site.register(SeriesData)