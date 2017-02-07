from django.db import models

# album Class
class Album(models.Model):
    artists = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

# song class
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    filr_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
