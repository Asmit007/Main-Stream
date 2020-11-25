from django.db import models

# Create your models here.


class MovieData(models.Model):
    title = models.CharField(max_length=500, default="")
    releasedON = models.DateField()
    desc = models.TextField(max_length=500, default="")
    platform = models.CharField(max_length=500)
    poster = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

class SeriesData(models.Model):
    title = models.CharField(max_length=500, default="")
    releasedON = models.DateField()
    desc = models.TextField(max_length=500, default="")
    platform = models.CharField(max_length=500)
    poster = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title
