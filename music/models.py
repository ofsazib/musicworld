from django.db import models
from django.contrib.auth.models import Permission, User

# album Class
class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artists = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)



    # method to show object
    def __str__(self):
        return self.album_title + ' - ' + self.artists

# song class
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
