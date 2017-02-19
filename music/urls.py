from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/ homepage
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),
    #  /login_user
    url(r'^login_user/$', views.login, name='login_user'),
    #  /logout_user
    url(r'^logout_user/$', views.register, name='logout_user'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # favorite_song
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    url(r'album/(?P<pk>[0-9]+)/create_song/$', views.SongCreate.as_view(), name='create_song'),
]
