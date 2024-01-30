from django.db import models

# Create your models here.
class Artist(models.Model):
     name = models.CharField(max_length=220)
     bio = models.TextField(blank=True, null=True)
     artist_img = models.ImageField(upload_to='artists_images/')
     
class Album(models.Model):
     title = models.CharField(max_length=225)
     released_date = models.DateField()
     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
     
class Song(models.Model):
     title = models.CharField(max_length=100)
     duration = models.DurationField()
     album = models.ForeignKey(Album, on_delete=models.CASCADE)         