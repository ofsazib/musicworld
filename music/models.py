from django.db import models

# album Class
class Album(models.Model):
    artists = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # method to show object
    def __str__(self):
        return self.album_title + ' - ' + self.artists

# song class
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
