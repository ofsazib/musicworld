from django.contrib.auth.models import User
from django import forms
from .models import Album, Song

#  Class for user register form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#  Class for AlbumCreate
class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artists', 'album_title', 'genre', 'album_logo']

#  Classs for add song
class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
