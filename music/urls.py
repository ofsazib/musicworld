from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/ homepage
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),
    #  /login_user
    url(r'^login_user/$', views.login_user, name='login_user'),
    #  /logout_user
    url(r'^logout_user/$', views.register, name='logout_user'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # favorite_song
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # filter song
    url(r'^songs/(?P<filter_by>[a-zA-Z]+)/$', views.songs, name='songs'),

    # create_album
    url(r'^create_album/$', views.create_album, name='create_album'),
    #  create song
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # delete song
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    #  favorite album
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    # delete album
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

]
