from django.db import models
from django.utils import timezone

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='artist_images/', blank=True)
    
    def __str__(self):
         return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='album_covers/', blank=True)
    
    def __str__(self):
         return self.title

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.DurationField()
    lyrics = models.TextField(blank=True)
    image = models.ImageField(upload_to='song_images/', blank=True)
    audio_file = models.FileField(upload_to='audio_files/')
    plays = models.IntegerField(default=0)  # New field for tracking number of plays
    
    def __str__(self):
         return self.title