from django.db import models

# Create your models here.

class MovieData(models.Model):
    title = models.CharField(max_length=500, default="")
    releasedON = models.DateField(null=True,blank=True)
    desc = models.TextField(max_length=5000, default="")
    platform = models.CharField(max_length=500,null=True, blank=True)
    poster = models.ImageField(upload_to = 'images/')
    trailer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title

class SeriesData(models.Model):
    title = models.CharField(max_length=500, default="")
    releasedON = models.DateField(null=True,blank=True)
    desc = models.TextField(max_length=5000, default="")
    platform = models.CharField(max_length=500,null=True, blank=True)
    poster = models.ImageField(upload_to = 'images/')
    trailer = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title
